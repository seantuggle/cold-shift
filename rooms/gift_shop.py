# rooms/gift_shop.py
# Room 3: Gift Shop & Café
# Closed for the night. Maya has gone home.
# The good coffee is waiting.

from items import Item, ConsumableItem, ContainerItem
from room import Room


# ---------------------------------------------------------------------------
# ITEMS
# ---------------------------------------------------------------------------

# --- Café Counter ---

class _MayasCoffee(ConsumableItem):
    """The coffee Maya left for Nick. No talisman — just go-juice."""
    def on_take(self, state):
        base = super().on_take(state)
        if self.taken:
            return (
                base + "\n\n"
                "The sticky note says NICK in rounded, careful handwriting.\n\n"
                "You stand there holding it for a second longer than you need to.\n\n"
                "It\'s just coffee. You know it\'s just coffee.\n\n"
                "You drink it anyway."
            )
        return base

    def on_drink(self, state):
        return self.on_eat(state)

    def on_eat(self, state):
        base = ConsumableItem.on_eat(self, state)
        if base:
            return base
        self.consumed = True
        return (
            "It\'s good coffee.\n\n"
            "Not the burnt, institutional kind from the security office pot. "
            "Actual good coffee — dark, clean, a little bitter in a way "
            "that makes sense.\n\n"
            "Maya said she left the good stuff in the back.\n\n"
            "She wasn\'t wrong.\n\n"
            "You drink it slowly. The blizzard presses at the windows. "
            "You don\'t think about anything for about forty-five seconds.\n\n"
            "That\'s the best you\'ve done in a while.\n\n"
            "You drop the empty cup in a trash can somewhere between here "
            "and wherever you\'re going next. It\'s a cup. It was good coffee. "
            "That\'s enough."
        )

mayas_coffee = _MayasCoffee(
    name="coffee",
    aliases=[
        "mayas coffee", "maya\'s coffee", "good coffee",
        "cup", "cup of coffee", "nick\'s coffee", "nicks coffee",
    ],
    description=(
        "A to-go cup sitting behind the café counter, "
        "capped with a lid, still warm.\n\n"
        "There\'s a sticky note on the side: NICK.\n\n"
        "In rounded, careful handwriting.\n\n"
        "Maya left it for you. She said she would. "
        "You weren\'t entirely sure she meant it.\n\n"
        "She meant it."
    ),
    eat_text="",
    hunger_reset=40,
    takeable=True,
)


# --- Merchandise Display ---

plush_whale = Item(
    name="plush whale",
    aliases=["whale", "stuffed whale", "plush", "toy whale", "toy"],
    description=(
        "A stuffed felt whale, about the size of a football. "
        "Blue, stitched smile, little embroidered eye.\n\n"
        "The tag says: MISKATONIC MUSEUM — FRIENDS OF THE DEEP.\n\n"
        "Fourteen ninety-nine.\n\n"
        "You put it in your pocket. It doesn\'t entirely fit. "
        "You make it fit."
    ),
    takeable=True,
)


class _SnowGlobe(Item):
    """
    Snow globe. Progressive text across three acts.
    Act 1: quiet nostalgia.
    Act 2: something feels wrong about the little museum inside.
    Act 3: the thing inside the globe is not the museum anymore.
    """
    def on_examine(self, state):
        act = getattr(state, "act", 1)
        visits = getattr(state, "snow_globe_visits", 0)
        state.snow_globe_visits = visits + 1

        if act == 1:
            if visits == 0:
                return (
                    "A snow globe. Museum souvenir — inside it, a tiny replica "
                    "of the Miskatonic Museum building, complete with a miniature "
                    "whale skeleton visible through a painted window.\n\n"
                    "You shake it.\n\n"
                    "The fake snow swirls. Settles. The little building "
                    "sits there, perfect and contained and impervious.\n\n"
                    "You had one of these as a kid. Different building. "
                    "Same idea. Same feeling, actually — "
                    "watching something small and whole and untouchable "
                    "from the outside.\n\n"
                    "You set it back down carefully."
                )
            elif visits == 1:
                return (
                    "You pick it up again.\n\n"
                    "Shake it. Watch it.\n\n"
                    "The museum inside looks warm. It isn\'t. "
                    "You know this because you are currently inside it "
                    "and it is December and the blizzard is winning.\n\n"
                    "But in there it looks warm.\n\n"
                    "You put it back."
                )
            else:
                return (
                    "You\'ve looked at it enough.\n\n"
                    "Some things don\'t get better the more you look at them.\n\n"
                    "Some things do. You\'re not sure which kind this is.\n\n"
                    "You leave it alone."
                )

        elif act == 2:
            return (
                "You pick up the snow globe again.\n\n"
                "Shake it.\n\n"
                "The snow swirls — but slower than it should. "
                "Like it\'s moving through something thicker than water.\n\n"
                "You look at the little museum inside.\n\n"
                "The whale skeleton in the painted window "
                "is facing a different direction than it was before.\n\n"
                "You put it down.\n\n"
                "You tell yourself you\'re misremembering."
            )

        else:  # act == 3
            return (
                "You pick up the snow globe.\n\n"
                "You don\'t shake it this time.\n\n"
                "The snow is moving anyway.\n\n"
                "The building inside is wrong. "
                "Not wrong like a bad replica — wrong like it was never "
                "a replica of this building. "
                "The proportions are off. The windows are in the wrong places. "
                "There is no whale skeleton visible inside it.\n\n"
                "There is something else.\n\n"
                "You set it down very carefully and do not look at it again.\n\n"
                "It was never just a snow globe.\n\n"
                "You don\'t know what it was."
            )

snow_globe = _SnowGlobe(
    name="snow globe",
    aliases=["globe", "snowglobe", "souvenir"],
    description="A snow globe with a tiny museum inside.",
    takeable=True,
)


# --- Pastry Case ---

class _Muffin(ConsumableItem):
    """One sad muffin. Nick eats it."""
    def on_eat(self, state):
        base = super().on_eat(state)
        if base:
            return base
        return (
            "Blueberry. Probably. It\'s hard to tell — "
            "it\'s been in the case since at least this morning "
            "and has achieved the specific density of a museum artifact.\n\n"
            "You eat it anyway.\n\n"
            "It tastes like blueberry and time.\n\n"
            "You\'ve had worse. Tonight, specifically, you\'ve had worse."
        )

muffin = _Muffin(
    name="muffin",
    aliases=["blueberry muffin", "pastry", "baked good"],
    description=(
        "A blueberry muffin sitting alone in the pastry case.\n\n"
        "It has been here for a while. "
        "It is making the best of the situation."
    ),
    eat_text="",
    hunger_reset=20,
    takeable=True,
)

pastry_case = ContainerItem(
    name="pastry case",
    aliases=["case", "display case", "glass case", "pastry display"],
    description=(
        "A glass-fronted pastry case on the café counter. "
        "The kind that\'s supposed to be full of things.\n\n"
        "It is not full of things."
    ),
    contents=[muffin],
)


# --- Tip Jar ---

class _TipJar(Item):
    """Tip jar. Nick doesn\'t take it. His internal voice won\'t let him."""
    def on_examine(self, state):
        return (
            "A glass jar on the counter with a strip of masking tape "
            "that says TIPS :) in marker.\n\n"
            "Inside: a few dollar bills, some quarters, a dime, "
            "and what appears to be a token from a Chuck E. Cheese "
            "that closed in 2009.\n\n"
            "You think about what twelve dollars in your wallet "
            "and a security guard salary looks like going forward.\n\n"
            "You leave the jar alone.\n\n"
            "You are not the kind of person who takes tip jars. "
            "You\'ve decided this just now, firmly, "
            "with the conviction of a man who needed to decide something."
        )

    def on_take(self, state):
        return (
            "You reach for it.\n\n"
            "Your hand actually gets there.\n\n"
            "And then — nothing dramatic, no voice from the sky — "
            "you just hear yourself, very clearly, "
            "saying \'no\' inside your own head.\n\n"
            "Not tonight. Not this.\n\n"
            "You put your hand back in your pocket."
        )

tip_jar = _TipJar(
    name="tip jar",
    aliases=["tips", "jar", "tip"],
    description="A glass jar of tips on the café counter.",
    takeable=False,
)


# --- Floor / Tables ---

class _Receipt(Item):
    """
    A dropped receipt. Total is $13.90 (rounds to 1890 — Lovecraft birth year).
    Coffee x2 + Danish. Handwriting at the bottom: ...crate...
    """
    def on_read(self, state):
        return (
            "MISKATONIC MUSEUM GIFT SHOP & CAFÉ\n"
            "─────────────────────────────────────\n"
            "  Coffee (drip)                $3.00\n"
            "  Coffee (latte, oat milk)     $5.00\n"
            "  Danish                       $4.75\n"
            "─────────────────────────────────────\n"
            "  SUBTOTAL                    $12.75\n"
            "  TAX                          $1.15\n"
            "  TOTAL                       $13.90\n\n"
            "  CASH TENDERED               $20.00\n"
            "  CHANGE                       $6.10\n\n"
            "  Thank you for visiting!\n"
            "  Your purchase supports museum programs.\n\n"
            "─────────────────────────────────────\n"
            "  [something handwritten at the bottom —\n"
            "   the ink is smeared, most of it illegible.\n"
            "   You can make out one word.]\n\n"
            "         ...crate...\n\n"
            "You look at it for a moment.\n\n"
            "You put the receipt in your pocket."
        )

receipt = _Receipt(
    name="receipt",
    aliases=["lost receipt", "paper", "slip"],
    description=(
        "A receipt on the floor near a café table. "
        "Someone dropped it on the way out."
    ),
    takeable=True,
)


class _Paperback(Item):
    """Forgotten paperback. Nick judges it. Pockets it anyway."""
    def on_read(self, state):
        return (
            "You flip it over and read the back cover.\n\n"
            "\"When marine biologist DR. CASSANDRA VOSS discovers "
            "a signal coming from the deepest part of the ocean, "
            "she doesn\'t expect it to be a response. "
            "A response to what? No one has been transmitting. "
            "No one human, anyway.\"\n\n"
            "You read that again.\n\n"
            "You are currently working a night shift in a natural history museum "
            "that contains, among other things, a whale skeleton and a crate "
            "your supervisor told you not to touch.\n\n"
            "You put the book down.\n\n"
            "You pick it back up.\n\n"
            "You put it in your pocket. "
            "You need something to do during the next Karen call."
        )

paperback = _Paperback(
    name="paperback",
    aliases=["book", "novel", "paperback book", "left book"],
    description=(
        "A paperback novel left on one of the café chairs. "
        "Someone got up and didn\'t come back for it.\n\n"
        "The cover shows a dark ocean and a single light "
        "coming from somewhere very far down."
    ),
    takeable=True,
)


# --- Tote Bag ---

class _ToteBag(Item):
    def on_examine(self, state):
        return (
            "A canvas tote bag with the museum logo on it — "
            "the whale skeleton, rendered in navy blue, "
            "with MISKATONIC MUSEUM OF NATURAL HISTORY below it.\n\n"
            "Eighteen dollars.\n\n"
            "You think about whether you need a tote bag.\n\n"
            "You think about what it would mean to be the kind of person "
            "who needs a tote bag.\n\n"
            "You are a security guard in an empty museum at midnight "
            "in a blizzard.\n\n"
            "You probably need a tote bag. "
            "You probably need a lot of things.\n\n"
            "You leave it where it is."
        )

    def on_take(self, state):
        result = super().on_take(state)
        if self.taken:
            return result + (
                "\n\nYou take the tote bag. "
                "You\'re going to put things in it. "
                "You\'re not sure what things yet. "
                "That\'s fine. That\'s growth."
            )
        return result

tote_bag = _ToteBag(
    name="tote bag",
    aliases=["tote", "bag", "museum bag", "canvas bag"],
    description="A canvas museum tote. Navy whale logo. Eighteen dollars.",
    takeable=True,
)


# --- Wall ---

class _Chalkboard(Item):
    """Café menu chalkboard. Maya wrote the note at the bottom."""
    def on_examine(self, state):
        return self.on_read(state)

    def on_read(self, state):
        return (
            "MISKATONIC MUSEUM CAFÉ\n"
            "════════════════════════════════\n\n"
            "  ☕  COFFEE & ESPRESSO\n"
            "  Drip Coffee           $3.00\n"
            "  Americano             $4.00\n"
            "  Latte                 $5.00\n"
            "  Cappuccino            $5.00\n"
            "  Cold Brew             $5.50\n\n"
            "  🍵  TEA\n"
            "  Hot Tea (assorted)    $3.00\n\n"
            "  🥣  SOUP OF THE DAY\n"
            "  Butternut Squash      $7.00\n"
            "    (served with bread)\n\n"
            "  🥐  PASTRIES\n"
            "  See display case\n\n"
            "════════════════════════════════\n"
            "  Proceeds support museum education programs.\n"
            "  Thank you for visiting!\n\n"
            "At the bottom of the board, in smaller, rounder handwriting — "
            "Maya\'s, you\'d guess — someone has added:\n\n"
            "  p.s. the good stuff is in the back. ask nicely :)\n\n"
            "You weren\'t going to ask. "
            "You called her instead.\n\n"
            "Same result."
        )

chalkboard = _Chalkboard(
    name="chalkboard",
    aliases=["menu", "board", "chalk board", "chalk menu", "cafe menu", "café menu"],
    description="The café menu, written on a wall-mounted chalkboard.",
    takeable=False,
)


# --- Pamphlet Rack ---

class _Pamphlets(Item):
    """Upcoming events. Gets increasingly ominous the more you read."""
    def on_examine(self, state):
        return (
            "A wire rack near the door holds a selection of pamphlets — "
            "museum membership information, exhibition guides, "
            "and a tri-fold for upcoming events.\n\n"
            "The membership one has a photo of happy people "
            "standing in front of the whale skeleton, smiling.\n\n"
            "They look like people who don\'t know what\'s in the crate."
        )

    def on_read(self, state):
        return (
            "UPCOMING EVENTS AT THE MISKATONIC MUSEUM\n\n"
            "  ◆  DEC 21 — Winter Solstice Family Night\n"
            "     Activities, crafts, and a special presentation:\n"
            "     \'The Longest Night: Darkness in Ancient Cultures\'\n"
            "     6 PM – 9 PM  |  Free with admission\n\n"
            "  ◆  DEC 26 – JAN 3 — The Deep Exhibition\n"
            "     A survey of oceanic life from the Cambrian to present.\n"
            "     Special display: artifacts recovered from the 1923\n"
            "     Miskatonic Antarctic Expedition.  [NEW ACQUISITION]\n\n"
            "  ◆  JAN 14 — Lecture: \'They That Dwell Beneath\'\n"
            "     Dr. H. Armitage, Miskatonic University\n"
            "     \'Pre-human civilization and the archaeological record\'\n"
            "     RSVP required. Seating is extremely limited.\n\n"
            "  ◆  FEB — EXHIBIT TBD\n"
            "     [This section of the pamphlet is blank\n"
            "      except for a small ink stain\n"
            "      that is, if you tilt it, shaped like nothing\n"
            "      you want to keep looking at.]\n\n"
            "You fold the pamphlet and put it back.\n\n"
            "The January lecture sounds like a fun night out.\n\n"
            "You are lying to yourself."
        )

pamphlets = _Pamphlets(
    name="pamphlets",
    aliases=["pamphlet", "brochure", "brochures", "rack", "flyer", "flyers", "events"],
    description="A wire rack of museum pamphlets near the door.",
    takeable=False,
)


# ---------------------------------------------------------------------------
# ROOM STRINGS
# ---------------------------------------------------------------------------

GIFT_SHOP_LONG = (
    "The gift shop is closed.\n\n"
    "Emergency lighting only — a pale amber strip along the baseboard "
    "that makes everything look like the end of something. "
    "The main lights are off. The refrigeration unit under the counter "
    "hums steadily, the only sound in here that doesn\'t feel like waiting.\n\n"
    "To your left, the café counter runs the length of the wall: "
    "espresso machine dormant, pastry case mostly empty, "
    "tip jar on the counter. A chalkboard menu hangs above it, "
    "handwritten. The soup of the day is butternut squash.\n\n"
    "To your right, a display case holds museum merchandise — "
    "stuffed animals, tote bags, postcard sets. "
    "A shelf above it holds snow globes and novelty items. "
    "Chairs are stacked on the small round café tables "
    "except for one, near the window, where someone left a paperback.\n\n"
    "Through the window: the blizzard. It has gotten worse.\n\n"
    "The lobby is west. The Hall of Ancient Civilizations is east."
)

GIFT_SHOP_SHORT = (
    "The gift shop, closed and amber-lit. "
    "The refrigeration unit hums. "
    "Outside, the blizzard continues to make its point."
)

GIFT_SHOP_AMBIENT = [
    "The refrigeration unit under the café counter cycles on with a low hum. "
    "It is the most reliable thing in this building right now.",

    "The blizzard presses at the gift shop windows. "
    "The snow globe on the shelf catches the emergency light "
    "and holds it for a moment.",

    "You can still smell the coffee. "
    "Not the burnt kind from your office. "
    "The good kind. Maya\'s kind. "
    "It\'s going cold now, slowly, the way good things do.",

    "The stacked chairs cast long shadows across the café floor. "
    "You know they\'re just chairs. "
    "You count them anyway. There are eight. "
    "You only count seven the second time.",

    "The espresso machine ticks once as it cools. "
    "Outside, something in the storm shifts — "
    "a gust that shudders the glass — and then settles. "
    "The amber light doesn\'t flicker. "
    "This is somehow worse.",
]


# ---------------------------------------------------------------------------
# FIRST VISIT EVENT
# ---------------------------------------------------------------------------

def _first_visit(state):
    """Fires once when Nick enters the gift shop for the first time."""
    if getattr(state, "maya_positive", False):
        return (
            "You smell it before you find it.\n\n"
            "Coffee. Good coffee — not the security office kind. "
            "The kind you\'d pay actual money for.\n\n"
            "She said it was here. She said she put your name on it.\n\n"
            "The gift shop is dark and closed and the blizzard is getting worse "
            "and you\'re a week into a job that is already not what you expected, "
            "and there is a cup of coffee behind this counter with your name on it "
            "in careful handwriting.\n\n"
            "You stand in the doorway for a moment.\n\n"
            "Then you go get it."
        )
    else:
        return (
            "The gift shop is dark and smells like coffee and cinnamon "
            "and something faintly floral that you can\'t place.\n\n"
            "The amber emergency lighting makes everything look like "
            "a photograph from before things went wrong.\n\n"
            "The refrigeration unit hums. "
            "Outside, the blizzard is consolidating its position.\n\n"
            "Behind the café counter, there\'s a to-go cup "
            "with a sticky note on it.\n\n"
            "You can\'t read it from here."
        )


# ---------------------------------------------------------------------------
# FACTORY
# ---------------------------------------------------------------------------

def make_gift_shop():
    """Build and return the Gift Shop & Café room (Room 3)."""
    room = Room(
        name="Gift Shop & Café",
        short_desc=GIFT_SHOP_SHORT,
        long_desc=GIFT_SHOP_LONG,
        exits={},   # west -> main_lobby, east -> hall_of_civilizations wired in main.py
    )

    room.items = [
        mayas_coffee,
        tip_jar,
        pastry_case,
        muffin,
        chalkboard,
        plush_whale,
        tote_bag,
        snow_globe,
        receipt,
        paperback,
        pamphlets,
    ]

    room.ambient_messages = GIFT_SHOP_AMBIENT
    room.first_visit_event = _first_visit

    return room
