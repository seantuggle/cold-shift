# engine/game_state.py
# Central truth for all game flags and counters.
# Everything that needs to persist across rooms lives here.

class GameState:
    def __init__(self):
        # --- Move counter ---
        self.moves = 0

        # --- Hunger system ---
        self.hunger_level = 0          # 0=fine, 1=peckish, 2=hungry, 3=starving
        self.moves_since_eating = 0
        self.HUNGER_INTERVAL = 20      # hunger ticks every 20 moves

        # --- Radio ---
        self.radio_on = False
        self.radio_taken = False

        # --- Karen ---
        self.karen_calls = 0           # how many times Karen has radioed
        self.last_karen_call = 0       # move number of last Karen call
        self.KAREN_INTERVAL = 30       # Karen checks in every 30 moves

        # --- Monitor state ---
        self.monitor_7_examined = False
        self.monitor_anomaly_seen = False  # mid-game monitor changes

        # --- Danny ---
        self.danny_found = False
        self.danny_note_read = False

        # --- Manuscript ---
        self.manuscript_found = False
        self.manuscript_read = False
        self.postit_reversed = False   # player figured out the anagram

        # --- Mask ---
        self.mask_found = False
        self.mask_worn = False
        self.mask_worn_turns = 0       # counts up; at 10 = death
        self.MASK_DEATH_TURNS = 10

        # --- Etching ---
        self.etching_taken = False
        self.etching_surface = None    # 'mask' or 'manuscript'
        self.has_paper = False

        # --- Portal ---
        self.blood_on_mask = False
        self.incantation_spoken = False
        self.portal_open = False

        # --- Maya ---
        self.maya_met = False
        self.maya_note_found = False
        self.maya_called = False
        self.phone_dead = False

        # --- General progression flags ---
        self.logbook_written = False
        self.radio_picked_up = False
        self.flashlight_on = False
        self.crate_examined = False
        self.vault_found = False

        # --- Ending ---
        self.game_over = False
        self.ending = None             # 'death_mask', 'death_carcosa', 'survived'

    def tick(self):
        """Call once per move. Updates hunger and Karen timers."""
        self.moves += 1
        self.moves_since_eating += 1
        self._update_hunger()
        self._check_karen()

    def _update_hunger(self):
        if self.moves_since_eating >= self.HUNGER_INTERVAL * 4:
            self.hunger_level = 3
        elif self.moves_since_eating >= self.HUNGER_INTERVAL * 3:
            self.hunger_level = 2
        elif self.moves_since_eating >= self.HUNGER_INTERVAL * 2:
            self.hunger_level = 1
        else:
            self.hunger_level = 0

    def _check_karen(self):
        """Returns True if Karen should interrupt this move."""
        if self.moves - self.last_karen_call >= self.KAREN_INTERVAL:
            return True
        return False

    def eat(self, reset_amount):
        """Call when player consumes food. reset_amount in moves."""
        self.moves_since_eating = max(0, self.moves_since_eating - reset_amount)
        self._update_hunger()

    def get_hunger_message(self):
        """Returns hunger flavor text appropriate to current level, or None."""
        # Only fire at the exact interval boundaries
        if self.moves_since_eating == self.HUNGER_INTERVAL:
            return (
                "Your stomach makes a noise that the empty museum "
                "politely ignores."
            )
        elif self.moves_since_eating == self.HUNGER_INTERVAL * 2:
            return (
                "You haven't eaten since — actually, when did you eat? "
                "Today feels like it happened to someone else."
            )
        elif self.moves_since_eating == self.HUNGER_INTERVAL * 3:
            return (
                "The hunger is a specific, insistent thing now. "
                "Less background noise, more main event."
            )
        elif self.moves_since_eating >= self.HUNGER_INTERVAL * 4:
            if self.moves_since_eating % self.HUNGER_INTERVAL == 0:
                return (
                    "You are operating on caffeine, spite, and whatever "
                    "psychic residue the museum is pumping through the vents. "
                    "This is fine."
                )
        return None
