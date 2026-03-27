# engine/game_state.py
# COLD SHIFT — global game state

class GameState:
    def __init__(self):

        # --- Core ---
        self.moves = 0
        self.game_over = False

        # --- Karen ---
        self.last_karen_call = 0
        self.KAREN_INTERVAL = 15
        self.karen_calls = 0

        # --- Equipment ---
        self.radio_taken = False
        self.radio_on = False
        self.flashlight_on = False

        # --- Puzzle flags ---
        self.postit_reversed = False
        self.logbook_written = False
        self.donations_opened = False
        self.wait_count = 0

        # --- Maya ---
        self.maya_called = False
        self.maya_met = False
        self.lobby_entered = False
        self.maya_coffee_given = False
        self.maya_positive = False

        # --- Act system ---
        self.act = 1

        # --- Item state ---
        self.snow_globe_visits = 0

        # --- Coin curse ---
        self.coin_pickup_turn = None  # set to state.moves when strange coin is taken

        # --- Gum ---
        self.gum_chewing = False      # True while Nick is chewing
        self.gum_chew_start = None    # state.moves when chewing began
        self.gum_consumed = False     # True once spat/discarded

        # --- Hunger ---
        self.hunger = 60

    def eat(self, n):
        """Reset hunger clock by n moves."""
        self.hunger += n

    def tick(self):
        """Called once per player action."""
        self.moves += 1
        if self.hunger > 0:
            self.hunger -= 1

    def get_hunger_message(self):
        """Returns a hunger warning string or None."""
        if self.hunger <= 0:
            return (
                "You are very hungry.\n\n"
                "This is not a metaphor. Your body is staging a formal complaint. "
                "You need to find something to eat. Soon. Like, now."
            )
        elif self.hunger <= 10:
            return (
                "Your stomach makes a sound.\n\n"
                "Not a polite sound. A sound that has opinions about your life choices. "
                "You should find food."
            )
        elif self.hunger <= 20:
            return (
                "You're getting hungry. "
                "The kind of hungry that makes everything slightly worse "
                "than it already is."
            )
        return None