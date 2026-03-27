# rooms/main_lobby.py
# The Main Lobby of the Miskatonic Museum.
# Grand, cold, and slightly wrong.
# The last place that feels like the normal world.

from room import Room
from items import Item, ConsumableItem


# ---------------------------------------------------------------------------
# MAYA LINES — rotate through these on TALK TO MAYA
# ---------------------------------------------------------------------------

MAYA_LINES = [
    (
        "Maya looks up from winding her scarf. \"First week and you already "
        "look like you've been here ten years. That's either a good sign "
        "or a bad one.\""
    ),
    (
        "\"You know the whale skeleton has a name?\" Maya nods upward. "
        "\"Staff calls her Margaret. Don't ask me why. She just looks "
        "like a Margaret.\""
    ),
    (
        "\"Massachusetts weather, I swear.\" Maya peers out at the blizzard "
        "beyond the chained doors. \"Four seasons in one day and then "
        "this shows up like it forgot to RSVP.\""
    ),
    (
        "\"You a Knicks fan?\" She reads something in your expression. "
        "\"Oh no.\" A pause. \"Oh, *no*. A Knicks fan. In my museum.\" "
        "She shakes her head slowly. \"Danny's already enough of a problem.\""
    ),
    (
        "\"I always feel like the building gets bigger at night,\" Maya says, "
        "almost to herself. \"Like it expands when nobody's looking.\"\n\n"
        "You tell her you know exactly what she means.\n\n"
        "She looks at you for a moment. \"Yeah. I think you do.\""
    ),
    (
        "\"The coffee in the break room is a crime against humanity. "
        "I left you the real stuff behind the counter — your name's on it.\" "
        "A pause. \"Don't tell Karen.\"\n\n"
        "You ask how she knows about the break room coffee.\n\n"
        "\"Everyone knows about the break room coffee, Nick. "
        "It's a museum. We study ancient things.\""
    ),
    (
        "Maya shoulders her bag, almost ready. \"I always feel bad for the "
        "exhibits, you know? Everything in here used to be somewhere else. "
        "Now it's just... here. Under fluorescent lights.\"\n\n"
        "She glances up at Margaret.\n\n"
        "\"Even her.\""
    ),
    (
        "\"Delacruz, by the way.\" Maya says it without looking up "
        "from her bag. \"My last name. In case you needed that for "
        "official security purposes.\"\n\n"
        "A beat.\n\n"
        "\"You did not need that for official security purposes.\""
    ),
]

MAYA_COFFEE_EXCHANGE = (
    "Maya raises an eyebrow. \"You're asking the person who's leaving "
    "for the night to make you coffee.\"\n\n"
    "A pause.\n\n"
    "\"Yeah, okay.\"\n\n"
    "She disappears behind the gift shop counter for ninety seconds "
    "and comes back with something that smells like an actual coffee "
    "shop instead of a punishment.\n\n"
    "\"Don't say I never did anything for you.\"\n\n"
    "She writes something on the cup before handing it over. "
    "You look down.\n\n"
    "It says NICK. Spelled correctly.\n\n"
    "You feel something unfamiliar. It takes a moment to identify.\n\n"
    "It's okay. You feel okay."
)

MAYA_EXIT = (
    "Maya winds her scarf with the practiced efficiency of someone "
    "who has walked into a lot of winters.\n\n"
    "\"Alright.\" She shoulders her bag one last time, really leaving "
    "now. \"The museum is yours, Nick.\"\n\n"
    "She pushes through the staff exit beside the main entrance. "
    "A cold gust — you smell snow and city and night.\n\n"
    "The door closes.\n\n"
    "She's gone.\n\n"
    "The lobby is very large and very quiet.\n\n"
    "Margaret hangs overhead in the dark.\n\n"
    "Merry Christmas, Nick."
)


# ---------------------------------------------------------------------------
# WHALE PROGRESSION
# Indexed by room.whale_visits — call get_whale_desc(room) each time
# ---------------------------------------------------------------------------

WHALE_DESCRIPTIONS = [
    (
        "The blue whale skeleton hangs suspended from the ceiling "
        "on steel cables, her bones the color of old ivory. "
        "You knew she was large — you've seen her every day this week — "
        "but at night, alone, she seems larger. More present. "
        "More aware.\n\n"
        "The placard reads: BALAENOPTERA MUSCULUS. "
        "BLUE WHALE. APPROXIMATE AGE AT DEATH: 70 YEARS.\n\n"
        "You look up at her for a long moment.\n\n"
        "Did that whale always have teeth?"
    ),
    (
        "You look up at Margaret.\n\n"
        "One of the suspension cables looks frayed on the left side. "
        "You make a mental note to log it.\n\n"
        "The shadow the skeleton throws doesn't quite match "
        "the angle of the lobby lighting.\n\n"
        "You look at the shadow for longer than you mean to."
    ),
    (
        "You don't look up at the whale this time.\n\n"
        "You've decided not to.\n\n"
        "This feels like the right decision."
    ),
    (
        "You look up anyway. You told yourself you wouldn't.\n\n"
        "The teeth are definitely there. You don't know enough about "
        "whale anatomy to say whether that's wrong. You suspect it is.\n\n"
        "The eye sockets are not empty.\n\n"
        "You look away. You walk faster."
    ),
    (
        "Margaret hangs overhead. Just bones. Just cables. "
        "The eye sockets are empty again.\n\n"
        "You don't find this comforting."
    ),
]


def get_whale_desc(room):
    idx = min(room.whale_visits, len(WHALE_DESCRIPTIONS) - 1)
    return WHALE_DESCRIPTIONS[idx]


# ---------------------------------------------------------------------------
# ITEMS
# ---------------------------------------------------------------------------

whale = Item(
    name="whale",
    aliases=["whale skeleton", "margaret", "bones", "skeleton",
             "blue whale", "ceiling", "teeth"],
    description=WHALE_DESCRIPTIONS[0],
    takeable=False,
)

front_doors = Item(
    name="front doors",
    aliases=["doors", "door", "entrance", "main entrance",
             "glass doors", "chain", "padlock", "lock", "glass"],
    description=(
        "Heavy glass and steel, the kind of doors that exist to impress "
        "visiting dignitaries and school groups. Tonight they're chained "
        "shut with a padlock the size of your fist.\n\n"
        "Beyond the glass: white. Just white. The blizzard has erased "
        "the city. The parking lot, the street, the buildings across "
        "the way — all of it gone.\n\n"
        "There's just you and the museum and the dark and the snow.\n\n"
        "One of your keys fits the padlock. "
        "You are not going out there."
    ),
    takeable=False,
)

security_camera = Item(
    name="security camera",
    aliases=["camera", "cctv", "lobby camera", "channel 12",
             "camera mount"],
    description=(
        "A security camera mounted high on the east wall, "
        "angled to cover the main entrance.\n\n"
        "You check the number on the housing: Channel 12.\n\n"
        "You think about the monitors back in the security office. "
        "You go through all sixteen feeds in your head.\n\n"
        "No Channel 12.\n\n"
        "This camera isn't on your monitors.\n\n"
        "You wonder what it is on."
    ),
    takeable=False,
)

christmas_tree = Item(
    name="christmas tree",
    aliases=["tree", "xmas tree", "holiday tree",
             "decorations", "tinsel", "lights"],
    description=(
        "An artificial Christmas tree, seven feet tall, doing its job "
        "with the weary dignity of something that gets assembled "
        "every December whether it wants to or not.\n\n"
        "Tinsel. Lights, half of which are working. Glass balls "
        "in red and gold. A wooden star at the top.\n\n"
        "And one ornament near the middle that doesn't match the others.\n\n"
        "Yellow. Angular. A symbol pressed into the surface "
        "that your eyes don't want to stay on."
    ),
    takeable=False,
)

yellow_ornament = Item(
    name="yellow ornament",
    aliases=["ornament", "yellow symbol", "strange ornament",
             "yellow", "odd ornament", "angular ornament", "symbol ornament"],
    description=(
        "You take it off the branch and hold it up.\n\n"
        "It's heavier than it looks. The material isn't glass — "
        "something older, smoother. The yellow is the color of "
        "old paper, of things left in the sun too long.\n\n"
        "The symbol pressed into it is angular, recursive — "
        "it seems to fold back on itself in a way that makes "
        "your eyes want to slide off it.\n\n"
        "You don't know what it means.\n\n"
        "You hang it back on the tree.\n\n"
        "When you let go, it turns slowly on its hook "
        "until the symbol faces you.\n\n"
        "You leave it alone."
    ),
    takeable=False,
)

museum_map = Item(
    name="museum map",
    aliases=["map", "directory", "museum directory", "sign",
             "information desk", "info desk", "board", "floor map",
             "information"],
    description=(
        "A large printed map behind perspex on the information desk.\n\n"
        "MISKATONIC MUSEUM OF NATURAL HISTORY AND ANTIQUITIES\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "GROUND FLOOR\n"
        "  Main Lobby                    [you are here]\n"
        "  Gift Shop & Cafe              [east]\n"
        "  Hall of Ancient Civilizations [west]\n\n"
        "UPPER FLOORS\n"
        "  Natural History Wing          [north, upper level]\n"
        "  Reading Room & Archive        [north, upper level]\n\n"
        "STAFF ONLY\n"
        "  Staff Corridors               [staff access]\n"
        "  Sub-Basement / Mechanical     [staff access]\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "At the very bottom, in small handwriting partially "
        "obscured by the frame:\n\n"
        "   Sub-Level Archive — Restricted\n\n"
        "No room number. No floor indicator. No further information.\n\n"
        "It's not on the map itself. Just the legend.\n\n"
        "You stare at it for a moment. You move on."
    ),
    takeable=False,
)

donations_box = Item(
    name="donations box",
    aliases=["donation box", "donations", "donation",
             "collection box", "perspex box"],
    description=(
        "A locked perspex box on a stand near the entrance, "
        "half full of the casual generosity of museum visitors.\n\n"
        "Loose bills. A handful of coins. A Canadian quarter "
        "that got in by mistake. A child's crayon drawing of "
        "what might be the whale or might be a large sad cloud.\n\n"
        "And at the bottom, something that doesn't catch the light "
        "the way coins should.\n\n"
        "A dark disc. Slightly larger than a quarter. "
        "No markings visible from here.\n\n"
        "The box is locked. And yet somehow the dark disc "
        "is now in your hand."
    ),
    takeable=False,
)

strange_coin = Item(
    name="strange coin",
    aliases=["coin", "dark coin", "disc", "strange disc",
             "token", "weird coin", "dark disc", "cold coin"],
    description=(
        "Quarter-sized, dark metal, heavier than it should be. "
        "One side is perfectly smooth. The other has markings "
        "your fingers can feel but your eyes can't quite follow — "
        "they seem to shift when you look directly at them.\n\n"
        "It is cold. Not room-temperature cold. "
        "Cold like it has been somewhere else entirely.\n\n"
        "It doesn't warm up in your hand.\n\n"
        "It hasn't warmed up at all."
    ),
    takeable=True,
)

bench = Item(
    name="bench",
    aliases=["benches", "visitor bench", "seat", "seats", "wooden bench"],
    description=(
        "A row of wooden benches along the east wall, "
        "designed for visitor comfort by someone who has never "
        "needed to sit down.\n\n"
        "On the nearest one: a child's mitten (right hand), "
        "a museum pamphlet from three years ago, "
        "and a candy wrapper that has Danny's fingerprints "
        "all over it spiritually.\n\n"
        "You sit for a moment.\n\n"
        "The lobby is even larger from down here.\n\n"
        "You stand back up."
    ),
    takeable=False,
)

trash_can = Item(
    name="trash can",
    aliases=["trash", "garbage", "bin", "waste bin",
             "rubbish", "garbage can"],
    description=(
        "A cylindrical metal trash can near the information desk, "
        "half full of visitor debris — coffee cups, pamphlets, "
        "a granola bar wrapper from someone who ate it guiltily "
        "in front of the whale.\n\n"
        "Underneath it, half-hidden: a small leather case. "
        "Like the kind that holds a folding knife or multi-tool. "
        "Must have slid off someone's belt.\n\n"
        "Nobody's claimed it."
    ),
    takeable=False,
)

utility_knife = Item(
    name="utility knife",
    aliases=["knife", "pocket knife", "folding knife", "blade",
             "leather case", "tool", "multi tool", "belt knife"],
    description=(
        "A folding utility knife in a worn leather belt case. "
        "Good quality — the kind a contractor or tradesperson carries "
        "and sharpens regularly out of quiet pride.\n\n"
        "The blade is clean. Sharp.\n\n"
        "Someone dropped this and doesn't know they dropped it.\n\n"
        "You clip the case to your belt next to the radio.\n\n"
        "It feels like a practical decision. "
        "That's all it is."
    ),
    takeable=True,
)

staff_exit = Item(
    name="staff exit",
    aliases=["staff door", "side door", "exit door",
             "push bar", "staff access door"],
    description=(
        "A plain door beside the main entrance, staff access only. "
        "Push-bar release — no key required from inside.\n\n"
        "Cold air seeps around the frame.\n\n"
        "Maya went through here not long ago."
    ),
    takeable=False,
)

maya_coffee = ConsumableItem(
    name="maya's coffee",
    aliases=["good coffee", "maya coffee", "real coffee",
             "the good coffee", "coffee maya made"],
    description=(
        "The coffee Maya made you. Paper cup, NICK written on "
        "the side in her handwriting. Spelled correctly.\n\n"
        "It's still warm. It smells like an actual coffee shop."
    ),
    eat_text=(
        "You drink Maya's coffee.\n\n"
        "It's warm and real and tastes like someone made it "
        "specifically for you.\n\n"
        "Which is exactly what happened.\n\n"
        "You hold the empty cup for a moment before throwing it away.\n\n"
        "You keep the cup."
    ),
    hunger_reset=35,
    takeable=True,
)


# ---------------------------------------------------------------------------
# ROOM FACTORY
# ---------------------------------------------------------------------------

def make_main_lobby():
    long_desc = (
        "MAIN LOBBY\n\n"
        "The entrance hall of the Miskatonic Museum opens above you "
        "like a cathedral that gave up on God and invested in "
        "square footage instead. The ceiling disappears into darkness. "
        "Somewhere up there, a blue whale skeleton hangs suspended "
        "on steel cables, her bones the color of old ivory.\n\n"
        "The front doors are chained. Beyond the glass: white. "
        "Just white. The blizzard has erased the city.\n\n"
        "An information desk holds a museum map. Near the east wall, "
        "a Christmas tree blinks its half-working lights, "
        "one ornament near the middle catching the eye for reasons "
        "you can't immediately place. A donations box. "
        "A row of benches. A trash can with something underneath it.\n\n"
        "A security camera on the east wall watches the entrance. "
        "You don't remember its feed on your monitors.\n\n"
        "The staff exit is beside the main doors."
    )

    short_desc = (
        "MAIN LOBBY\n\n"
        "The whale hangs overhead. The blizzard presses at the doors. "
        "The Christmas tree blinks."
    )

    ambient = [
        "The whale's shadow shifts slightly across the marble floor. "
        "The heating vents, probably.",
        (
            "One of the Christmas tree lights blinks out. "
            "Comes back on. Blinks out again."
        ),
        "The blizzard gusts hard against the front doors. The glass flexes. Holds.",
        "The lobby is very quiet. It was designed to be impressive. "
        "At night it mostly succeeds at being large.",
        "You find yourself not looking at the whale. "
        "You're not sure exactly when you made that decision.",
        (
            "The yellow ornament on the Christmas tree turns slowly "
            "on its hook. There's no draft in here."
        ),
        "Margaret hangs in the dark overhead. Patient as she has been for forty years.",
    ]

    room = Room(
        name="Main Lobby",
        short_desc=short_desc,
        long_desc=long_desc,
        exits={
            "south": None,
            "east": None,
            "west": None,
        },
    )

    room.ambient_messages = ambient

    # Lobby-specific state
    room.whale_visits = 0
    room.maya_moves = 0
    room.maya_present = False
    room.maya_left = False
    room.maya_coffee_given = False
    room.maya_line_index = 0

    room.items = [
        whale, front_doors, security_camera,
        christmas_tree, yellow_ornament,
        museum_map, donations_box, strange_coin,
        bench, trash_can, utility_knife,
        staff_exit,
    ]

    return room
