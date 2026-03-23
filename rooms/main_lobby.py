# rooms/main_lobby.py
# The Main Lobby. Crossroads of the museum.
# The last place that feels like the normal world.
# The whale is here. Maya is here — if Nick is quick enough.

from room import Room
from items import Item, ConsumableItem


# ---------------------------------------------------------------------------
# ITEMS
# ---------------------------------------------------------------------------

whale = Item(
    name="whale",
    aliases=["whale skeleton", "skeleton", "bones", "blue whale",
             "whale bones", "jaw", "cables"],
    description=(
        "Forty-seven feet. The placard on the wall says forty-seven feet, "
        "as if the number explains the feeling.\n\n"
        "It doesn't.\n\n"
        "The bones are the color of old piano keys. The cables holding it "
        "look thin from down here, but you assume someone calculated this. "
        "Someone ran the numbers. Someone signed off.\n\n"
        "You look at the jaw.\n\n"
        "You look away."
    ),
    takeable=False,
)

whale_teeth = Item(
    name="teeth",
    aliases=["whale teeth", "jaw teeth", "fangs"],
    description=(
        "The placard says blue whale.\n\n"
        "Blue whales don't have teeth.\n"
        "Blue whales are baleen whales.\n\n"
        "You know this. You don't know how you know this, but you know this.\n\n"
        "You look at the teeth.\n\n"
        "The placard still says blue whale.\n\n"
        "You walk away."
    ),
    takeable=False,
)

front_doors = Item(
    name="front doors",
    aliases=["doors", "door", "entrance", "exit", "front door", "glass doors"],
    description=(
        "The doors are chained from the inside with a padlock the size "
        "of your fist. Through the glass: nothing. White. "
        "The blizzard has been thorough.\n\n"
        "You try the handle anyway.\n\n"
        "Locked. Obviously locked. You're a security guard who just tried "
        "a locked door he locked himself an hour ago.\n\n"
        "This is fine."
    ),
    takeable=False,
)

chain = Item(
    name="chain",
    aliases=["padlock", "lock", "door chain"],
    description=(
        "Heavy chain, industrial padlock. "
        "The key is on your ring — you remember locking up at 11.\n\n"
        "Locked from the inside. Nobody gets in.\n"
        "Nobody gets out.\n\n"
        "You find this reassuring for exactly as long as it takes "
        "to remember you're the nobody."
    ),
    takeable=False,
)

security_camera = Item(
    name="security camera",
    aliases=["camera", "dome camera", "cctv camera", "red light"],
    description=(
        "Standard dome camera, northeast corner. "
        "Red light steady. Active.\n\n"
        "You go through your monitor feeds mentally. "
        "Loading dock. Gift shop. Rotunda. "
        "East corridor. West corridor.\n\n"
        "This camera is not on any of your feeds.\n\n"
        "You make a note. The note joins other notes. "
        "You have a lot of notes now and none of them are doing anything."
    ),
    takeable=False,
)

christmas_tree = Item(
    name="christmas tree",
    aliases=["tree", "xmas tree", "holiday tree", "decorated tree",
             "artificial tree"],
    description=(
        "A seven-foot artificial tree, pre-lit, decorated with the "
        "institutional determination of someone who was told to make it "
        "festive and did the minimum required.\n\n"
        "Silver tinsel. Glass balls in red and gold. "
        "A star on top that lists slightly to the left.\n\n"
        "And one ornament you don't recognize."
    ),
    takeable=False,
)

yellow_ornament = Item(
    name="ornament",
    aliases=["yellow ornament", "strange ornament", "weird ornament",
             "yellow symbol", "symbol ornament"],
    description=(
        "It's yellow — a pale, specific yellow, the yellow of old paper "
        "or certain kinds of sky.\n\n"
        "The shape carved into it is not a snowflake. Not a star. "
        "Not anything in the standard holiday vocabulary.\n\n"
        "You turn it over in your hands. "
        "It's heavier than it looks. "
        "The symbol means nothing to you.\n\n"
        "You hang it back on the tree.\n\n"
        "Later — much later — you'll see this symbol again. "
        "By then you'll know what it means.\n\n"
        "You'll wish you didn't."
    ),
    takeable=True,
)

directory = Item(
    name="directory",
    aliases=["museum directory", "map", "museum map", "sign",
             "wall directory", "exhibit map"],
    description=(
        "Mounted on the east wall, the museum directory "
        "lists the permanent collection wings:\n\n"
        "   MAIN LOBBY — Ground Floor\n"
        "   GIFT SHOP & CAFÉ — Ground Floor East\n"
        "   HALL OF ANCIENT CIVILIZATIONS — Ground Floor West\n"
        "   NATURAL HISTORY WING — Second Floor\n"
        "   READING ROOM & ARCHIVE — Second Floor East\n"
        "   STAFF CORRIDORS — Restricted\n"
        "   SUB-BASEMENT — Restricted\n\n"
        "And at the bottom, no room number, "
        "no floor designation, no asterisk:\n\n"
        "   SUB-LEVEL ARCHIVE\n\n"
        "That's all. Just the name. No arrow. No number. "
        "As if whoever made the sign felt obligated to include it "
        "but couldn't bring themselves to say where it was."
    ),
    takeable=False,
)

donations_box = Item(
    name="donations box",
    aliases=["donation box", "box", "donations", "donation"],
    description=(
        "A wooden box with a slot in the top and a small padlock "
        "you could open with one of your keys.\n\n"
        "It takes you three tries to talk yourself into it."
    ),
    takeable=False,
)

strange_coin = Item(
    name="strange coin",
    aliases=["coin", "weird coin", "cold coin", "unknown coin"],
    description=(
        "Both sides. Same face. Masked.\n\n"
        "You've been holding it for ten minutes and it's still cold. "
        "Your hand is warm. "
        "The coin is not interested in your warmth."
    ),
    takeable=True,
)

flattened_penny = Item(
    name="penny",
    aliases=["flattened penny", "pressed penny", "copper penny",
             "souvenir penny"],
    description=(
        "A flattened penny from the machine near the gift shop — "
        "the kind where you put in a dollar and a penny and crank "
        "the handle and get back an oval of copper "
        "with a picture pressed into it.\n\n"
        "This one has the whale.\n\n"
        "Of course it does."
    ),
    takeable=True,
)

bench = Item(
    name="bench",
    aliases=["lobby bench", "seat", "seating"],
    description=(
        "A wooden bench against the south wall, "
        "the kind designed to be looked at more than sat on. "
        "Cold. Hard. Unwelcoming in a specifically public way.\n\n"
        "Near its base, half-tucked under the rubber foot — "
        "a folding knife in a leather case."
    ),
    takeable=False,
)

folding_knife = Item(
    name="folding knife",
    aliases=["knife", "pocket knife", "penknife", "leather case",
             "knife case"],
    description=(
        "A folding knife in a worn leather case. "
        "Good quality, well-used, someone's everyday carry "
        "that slipped out of a pocket and never got claimed.\n\n"
        "The blade is clean. The edge is sharp.\n\n"
        "You pocket it without thinking too hard about why."
    ),
    takeable=True,
)

crowbar = Item(
    name="crowbar",
    aliases=["pry bar", "prybar", "bar", "iron bar"],
    description=(
        "A standard crowbar, heavy, black, slightly scuffed "
        "from actual use. Someone left it next to the trash can "
        "in the main lobby of a museum.\n\n"
        "Nobody leaves a crowbar by accident."
    ),
    takeable=True,
)

trash_can = Item(
    name="trash can",
    aliases=["trash", "garbage can", "bin", "waste bin", "rubbish bin"],
    description=(
        "A standard museum trash can, mostly empty. "
        "A coffee cup. A granola bar wrapper.\n\n"
        "Near the base, half-tucked under the can's rubber foot — "
        "a crowbar. Heavy, black, slightly scuffed."
    ),
    takeable=False,
)

placard = Item(
    name="placard",
    aliases=["whale placard", "sign", "whale sign", "information placard"],
    description=(
        "A brass placard mounted on a stand near the whale:\n\n"
        "   BALAENOPTERA MUSCULUS\n"
        "   Blue Whale\n"
        "   Cast from original specimen, 1987\n"
        "   Donated by the Hargrove Foundation\n\n"
        "Below that, in smaller text:\n"
        "   'The largest animal known to have ever existed.'\n\n"
        "You look up at the jaw.\n\n"
        "You look back at the placard.\n\n"
        "The placard says blue whale."
    ),
    takeable=False,
)

paper_cup = Item(
    name="paper cup",
    aliases=["cup", "coffee cup", "steam", "steaming cup"],
    description=(
        "A paper cup on the floor near the gift shop entrance. "
        "Still faintly warm.\n\n"
        "Maya's. She must have set it down while she put on her coat "
        "and forgotten it.\n\n"
        "Or left it on purpose.\n\n"
        "You pick it up. It's empty. "
        "It smells like a dirty chai with an extra shot.\n\n"
        "You hold it for longer than makes sense "
        "and then throw it away."
    ),
    takeable=False,
)


# ---------------------------------------------------------------------------
# MAYA
# ---------------------------------------------------------------------------

class MayaCharacter:
    """Maya — present only in the first 10 moves."""

    def __init__(self):
        self.present = True
        self.talked_to = False
        self.coffee_given = False
        self.hugged = False
        self.pepper_sprayed = False
        self.pepper_spray_turns = 0

    def leave(self, how="normal"):
        self.present = False
        self._how_left = how

    def on_talk(self, state):
        if not self.present:
            return "Maya is already gone."
        self.talked_to = True
        return (
            "You talk to her. It turns out to be easy — "
            "easier than it's been with anyone in a while.\n\n"
            "She asks how long you've been in security. "
            "You tell her: one week. She laughs.\n\n"
            "\"That explains the look on your face "
            "every time Karen comes on the radio.\"\n\n"
            "You ask how long she's been at the café. "
            "Three years, she says. She's finishing her degree at night. "
            "Art history. She likes the museum after hours — "
            "or she did, before she had to actually be in it after hours.\n\n"
            "\"It's different at night,\" she says. "
            "\"The building feels like it's thinking.\"\n\n"
            "She winds her scarf one more loop.\n\n"
            "\"Stay safe out there, Nick.\"\n\n"
            "She means it. You can tell when people mean it anymore. "
            "Most of them don't.\n\n"
            "She waves and heads out into the blizzard. "
            "The doors close. The lobby is immediately larger."
        )

    def on_coffee(self, state):
        if not self.present:
            return "Maya is already gone."
        self.coffee_given = True
        state.maya_met = True
        return (
            "\"Oh — yeah, absolutely.\"\n\n"
            "She disappears back into the gift shop for three minutes "
            "and returns with a paper cup, lid on, "
            "a little cardboard sleeve to protect your hand.\n\n"
            "\"Dirty chai, extra shot. "
            "You look like a dirty chai extra shot kind of situation.\"\n\n"
            "She remembered. You didn't realize you'd told her. "
            "Maybe you didn't — maybe she just looked at you and knew.\n\n"
            "You drink it while you walk her to the door. "
            "It's perfect. Warm and spiced and slightly too strong, "
            "exactly the way you like it.\n\n"
            "She buttons her coat. Waves once — "
            "two fingers, a small gesture.\n\n"
            "The doors close. The lobby is immediately larger."
        )

    def on_hug(self, state):
        if not self.present:
            return "Maya is already gone."
        self.hugged = True
        state.maya_called = True   # she won't answer the phone now
        return (
            "You take a step toward her with your arms doing a thing "
            "your brain didn't fully authorize.\n\n"
            "Maya takes a step back. Not unkind — just clear.\n\n"
            "\"Oh — I'm, that's — I'm not really...\" "
            "She trails off. Adjusts her scarf. "
            "Looks somewhere near your left shoulder.\n\n"
            "\"I should go. Roads are bad.\"\n\n"
            "She leaves quickly. The doors close.\n\n"
            "You stand in the lobby with your arms in a position "
            "they'll remember for a while.\n\n"
            "She doesn't answer when you call later. "
            "You'll understand why."
        )

    def on_kiss(self, state):
        if not self.present:
            return "Maya is already gone."
        self.pepper_sprayed = True
        self.pepper_spray_turns = 4
        state.maya_called = True   # she definitely won't answer now
        state.maya_met = False     # no note either
        return (
            "You lean in —\n\n"
            "Maya's hand moves with the speed and certainty of someone "
            "who has taken exactly one self-defense class "
            "and retained exactly one thing from it.\n\n"
            "The pepper spray hits you directly.\n\n"
            "You spend the next four turns unable to do anything except "
            "exist in a state of profound regret "
            "and eye-watering physical consequences.\n\n"
            "When you can see again, Maya is gone. "
            "The lobby smells faintly of capsaicin and poor decisions.\n\n"
            "You have not died.\n"
            "You have done something worse: "
            "you will remember this.\n\n"
            "(Vision impaired for 4 turns. "
            "Maya is gone. She will not answer the phone. "
            "There is no note.)"
        )

    def on_leave_without_interaction(self):
        """Fires if Maya leaves without Nick engaging."""
        return (
            "You stand near the door, watching the blizzard.\n\n"
            "Maya finishes winding her scarf. "
            "She looks over at you once — "
            "a look that might have been something "
            "if you'd said anything.\n\n"
            "\"Well —\" A pause. \"Bye. I guess.\"\n\n"
            "She says it quietly, almost to herself.\n\n"
            "The doors close. You can hear her footsteps "
            "on the other side, moving away, getting quieter, gone.\n\n"
            "The lobby is larger than it was."
        )


maya = MayaCharacter()


# ---------------------------------------------------------------------------
# ROOM FACTORY
# ---------------------------------------------------------------------------

# Whale visit counter — tracks progressive horror
_whale_visit_count = 0

SHORT_DESCS = [
    # Visit 2
    (
        "MAIN LOBBY\n\n"
        "The whale hangs. One of the support cables looks different "
        "than you remember — the angle is wrong, or the shadow is. "
        "You don't stop walking.\n\n"
        "Exits: South, East, West."
    ),
    # Visit 3
    (
        "MAIN LOBBY\n\n"
        "You don't look up this time.\n"
        "You've decided not to.\n\n"
        "Exits: South, East, West."
    ),
    # Visit 4 (late game dread)
    (
        "MAIN LOBBY\n\n"
        "You look up anyway. You always look up anyway.\n\n"
        "The teeth are definitely there.\n"
        "The eye sockets aren't empty.\n\n"
        "You walk faster.\n\n"
        "Exits: South, East, West."
    ),
    # Visit 5+ (post-Carcosa, or just repeated late)
    (
        "MAIN LOBBY\n\n"
        "Just bones. Just cable and darkness and old ivory.\n\n"
        "Nick stands under it for a long moment.\n\n"
        "He doesn't find this comforting.\n\n"
        "Exits: South, East, West."
    ),
]

AMBIENT_MESSAGES = [
    (
        "The whale hangs overhead. You don't look at it. "
        "You're getting good at not looking at it."
    ),
    (
        "The blizzard shifts against the glass — a sound like breathing, "
        "or like something very large turning over in its sleep."
    ),
    (
        "The security camera's red light blinks once. Just once. "
        "It was probably always doing that."
    ),
    (
        "The Christmas tree lights flicker in a pattern "
        "that isn't quite random. "
        "You decide not to count the intervals."
    ),
    (
        "In the quiet, the whale's cables make a sound. Barely. "
        "The sound of weight being held "
        "by something that might be reconsidering."
    ),
]


class MainLobbyRoom(Room):
    """
    Custom Room subclass for the Main Lobby.
    Handles whale progression and Maya's timed presence.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lobby_visits = 0
        self.maya_window_open = True   # closes after 10 player moves

    def describe(self, state):
        self.lobby_visits += 1

        if not self.visited:
            self.visited = True
            # First visit — check Maya window
            if self.maya_window_open and maya.present:
                desc = self.long_desc
                desc += "\n\n" + (
                    "Maya is still here.\n\n"
                    "She's near the entrance, pulling on a coat that looks "
                    "significantly warmer than yours, winding a scarf "
                    "around her neck with the practiced efficiency of someone "
                    "who has survived many winters. "
                    "Her dark curly hair catches the light as she turns.\n\n"
                    "She sees you and smiles. An unguarded smile — "
                    "the kind people stop doing after a while, "
                    "and she hasn't stopped yet.\n\n"
                    "\"Hey, security.\" A pause. \"Nick.\"\n\n"
                    "She says your name like she already decided "
                    "she was going to remember it.\n\n"
                    "Outside, the blizzard presses white against the glass. "
                    "Inside, for approximately thirty seconds, "
                    "everything is fine.\n\n"
                    "(You can TALK TO MAYA, ASK FOR COFFEE, or HUG MAYA.)"
                )
            elif not maya.present and not self.maya_window_open:
                # Missed Maya entirely
                desc = self.long_desc
                desc += "\n\n" + (
                    "Near the gift shop entrance, a paper cup sits "
                    "on the floor. Still steaming faintly.\n\n"
                    "Maya's already gone."
                )
            else:
                desc = self.long_desc
        else:
            # Return visits — progressive whale horror
            idx = min(self.lobby_visits - 2, len(SHORT_DESCS) - 1)
            desc = SHORT_DESCS[idx]

        # List takeable items
        visible = [
            i for i in self.items
            if not i.taken and not i.consumed
            and i.name not in ["whale", "teeth", "front doors", "chain",
                               "security camera", "christmas tree",
                               "directory", "donations box", "bench",
                               "trash can", "placard", "paper cup"]
        ]
        if visible:
            desc += "\n\nYou can see: " + ", ".join(
                f"a {i.name}" for i in visible
            ) + "."

        if self.exits:
            desc += "\n\nExits: " + ", ".join(
                d.capitalize() for d in self.exits
            ) + "."

        return desc

    def check_maya_timeout(self, moves):
        """Call each turn. If 10 moves passed and Maya still here, she leaves."""
        if self.maya_window_open and maya.present and moves >= 10:
            self.maya_window_open = False
            maya.leave(how="timeout")
            return maya.on_leave_without_interaction()
        return None


def make_main_lobby():
    """Build and return the fully populated Main Lobby."""

    long_desc = (
        "MAIN LOBBY\n\n"
        "The Miskatonic Museum opens above you like a cathedral that found "
        "square footage more interesting than God. "
        "The ceiling disappears into darkness thirty feet up. "
        "The marble floor reflects nothing — "
        "too old, too worn, too tired to give anything back.\n\n"
        "Suspended from the ceiling on cables that look, from down here, "
        "entirely too thin for the job — the blue whale skeleton. "
        "Forty-seven feet of bone and silence. "
        "It hangs in the dark the way large things hang in the dark: "
        "with complete indifference to whether you find it "
        "beautiful or terrible.\n\n"
        "It seems larger than it did this afternoon.\n"
        "You're not sure why.\n\n"
        "Did that whale always have teeth?\n\n"
        "The front doors are chained and padlocked at the far end. "
        "Through the glass: white. "
        "The blizzard has erased the street entirely. "
        "The museum is an island now, and you are on it.\n\n"
        "A Christmas tree stands near the donation box, decorated with "
        "the specific melancholy of institutional holiday cheer. "
        "A security camera watches from the northeast corner, "
        "its red light steady. "
        "A museum directory is mounted on the east wall. "
        "A bench sits against the south wall near a trash can."
    )

    room = MainLobbyRoom(
        name="Main Lobby",
        short_desc="",   # handled dynamically
        long_desc=long_desc,
        exits={
            "south": None,   # Security Office — wired in world.py
            "east": None,    # Gift Shop & Café — wired in world.py
            "west": None,    # Hall of Ancient Civilizations — wired in world.py
        },
    )

    room.ambient_messages = AMBIENT_MESSAGES

    room.items = [
        whale, whale_teeth, front_doors, chain,
        security_camera, christmas_tree, yellow_ornament,
        directory, donations_box, strange_coin, flattened_penny,
        bench, folding_knife, crowbar, trash_can,
        placard, paper_cup,
    ]

    return room
