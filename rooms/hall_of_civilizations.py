# rooms/hall_of_civilizations.py
# Room 4: Hall of Ancient Civilizations
# Where the horror begins in earnest.
# The crate is here. The mask is here. Danny was here.

from room import Room
from items import Item, ConsumableItem


# ---------------------------------------------------------------------------
# THE MASK — special item with 10-turn death mechanic
# Wearing it triggers degrading text in main.py
# ---------------------------------------------------------------------------

class _PallidMask(Item):
    def on_examine(self, state):
        if getattr(state, 'mask_worn', False):
            return (
                "It's on your face.\n\n"
                "You know it's on your face.\n\n"
                "You can feel it."
            )
        visits = getattr(state, 'mask_examine_count', 0)
        state.mask_examine_count = visits + 1

        if visits == 0:
            return (
                "It's pale. Not white — paler than white, the color of "
                "old bone left in sun too long.\n\n"
                "Theatrical. A mask meant to be worn — "
                "the kind of thing a prop department might make "
                "for a stage production, if the production were very old "
                "and the prop department had access to materials "
                "that don't have names in any catalog you've seen.\n\n"
                "The expression is — you can't quite say. "
                "It changes depending on the angle. "
                "Head-on it looks serene. "
                "From the left, something else. "
                "From the right, you look away.\n\n"
                "It has been lying on the floor a few feet from the crate. "
                "Danny was here. This was Danny's doing.\n\n"
                "You don't touch it. Not yet.\n\n"
                "Not yet."
            )
        elif visits == 1:
            return (
                "You look at it again.\n\n"
                "It's still pale. Still theatrical. "
                "Still doing that thing with the expression "
                "where you can't hold it in your peripheral vision "
                "without feeling like something is about to happen.\n\n"
                "There's a symbol on the interior surface — "
                "you can see it from this angle. "
                "The same symbol as the ornament on the Christmas tree.\n\n"
                "You file that away."
            )
        else:
            return (
                "The mask lies on the floor.\n\n"
                "You've looked at it enough to know "
                "you should stop looking at it.\n\n"
                "You look at it anyway."
            )

    def on_take(self, state):
        if getattr(state, 'mask_worn', False):
            return "It's already on your face."
        self.taken = True
        state.mask_location = 'inventory'
        return (
            "You pick it up.\n\n"
            "It's lighter than it looks. "
            "Much lighter. "
            "Like it doesn't weigh anything.\n\n"
            "It's cold in your hand. "
            "Not room-temperature cold — cold like the strange coin. "
            "Cold like something that has been somewhere else.\n\n"
            "You hold it at arm's length.\n\n"
            "The expression, head-on, is serene.\n\n"
            "You put it in your jacket pocket. "
            "It fits, somehow, despite everything."
        )

    def on_wear(self, state):
        if getattr(state, 'mask_worn', False):
            return "You're already wearing it."
        if not self.taken:
            return (
                "You'd need to pick it up first.\n\n"
                "Some part of you is glad you haven't."
            )
        state.mask_worn = True
        state.mask_worn_turns = 0
        state.mask_location = 'worn'
        return (
            "You raise the mask to your face.\n\n"
            "It fits perfectly. Of course it does.\n\n"
            "The world through the eyeholes is —\n\n"
            "different.\n\n"
            "Not wrong, exactly. Just — more. "
            "Like a frequency you weren't receiving before "
            "has suddenly resolved into signal.\n\n"
            "You see the Hall of Ancient Civilizations.\n\n"
            "You see what's in it.\n\n"
            "You see what's been in it all along."
        )

    def on_drop(self, state):
        if getattr(state, 'mask_worn', False):
            return "You can't drop something that's on your face."
        if not self.taken:
            return "You're not holding it."
        self.taken = False
        state.mask_location = 'floor'
        return (
            "You set the mask down on the floor.\n\n"
            "You step back from it.\n\n"
            "It looks different from down there. "
            "More patient."
        )


pallid_mask = _PallidMask(
    name="pallid mask",
    aliases=["mask", "pale mask", "white mask", "theatrical mask",
             "the mask", "pallid"],
    description="A pale theatrical mask lying on the floor near the crate.",
    takeable=True,
)


# ---------------------------------------------------------------------------
# THE CRATE
# ---------------------------------------------------------------------------

class _Crate(Item):
    def on_examine(self, state):
        if not getattr(state, 'crate_examined', False):
            state.crate_examined = True
            return (
                "The crate is large — shipping-container large, "
                "the kind that crosses oceans. "
                "It sits in the center of the hall, roped off "
                "with stanchions and yellow tape, "
                "a handwritten sign taped to the rope:\n\n"
                "   DO NOT TOUCH — K\n\n"
                "The crate is open.\n\n"
                "The lid has been removed — not forced, not broken. "
                "Set aside, leaned against the side, "
                "with the care of someone who intended to put it back. "
                "Danny intended to put it back.\n\n"
                "Inside: packing straw, mostly. "
                "The impression of something that was nested here, "
                "something roughly mask-shaped "
                "and something else — larger, flatter. "
                "Both gone now.\n\n"
                "On the side of the crate, stenciled in black, "
                "the letters worn and partially illegible:\n\n"
                "   _HE K__G _N __LL_W\n\n"
                "Some of the letters have flaked away with age. "
                "The ones that remain don't immediately "
                "resolve into anything.\n\n"
                "You don't touch it. Karen's note says not to.\n\n"
                "You've already touched it with your eyes "
                "more than you're comfortable with."
            )
        return (
            "The open crate, roped off. "
            "The straw packing inside still holds the shapes "
            "of what was in it.\n\n"
            "   _HE K__G _N __LL_W\n\n"
            "You look at the letters. "
            "You look away."
        )


crate = _Crate(
    name="crate",
    aliases=["shipping crate", "the crate", "wooden crate",
             "acquisition", "box"],
    description="A large open shipping crate, roped off with yellow tape.",
    takeable=False,
)


# ---------------------------------------------------------------------------
# MANUSCRIPT FRAGMENT
# ---------------------------------------------------------------------------

manuscript_fragment = Item(
    name="manuscript fragment",
    aliases=["fragment", "torn page", "page fragment", "paper fragment",
             "torn paper", "scrap", "page"],
    description=(
        "A torn corner of a page — heavy paper, very old, "
        "the kind of old that has a smell to it.\n\n"
        "The handwriting is dense and cramped, "
        "ink that should have faded centuries ago still "
        "somehow perfectly black.\n\n"
        "Three legible words in the fragment:\n\n"
        "   ...the Yellow King...\n\n"
        "The rest is torn away.\n\n"
        "You fold it carefully and put it in your pocket.\n\n"
        "Your pen, in your jacket pocket, feels slightly warm."
    ),
    takeable=True,
)


# ---------------------------------------------------------------------------
# DISPLAY CASES
# ---------------------------------------------------------------------------

class _CrackedCase(Item):
    def on_examine(self, state):
        visits = getattr(state, 'cracked_case_visits', 0)
        state.cracked_case_visits = visits + 1
        if visits == 0:
            return (
                "A tall glass display case running along the east wall, "
                "holding pre-Columbian ritual objects — "
                "small figurines, obsidian blades, "
                "a ceremonial bowl with geometric markings.\n\n"
                "The placard reads: PURPOSE UNKNOWN.\n\n"
                "The case is cracked — a long diagonal fracture "
                "running from the middle of the glass to the lower corner. "
                "Not fresh. Not recent. "
                "The kind of crack that happens when something "
                "bumps into a display case and doesn't mention it.\n\n"
                "Danny.\n\n"
                "The objects inside are undisturbed. "
                "Nothing got out.\n\n"
                "You look at the geometric markings on the bowl.\n\n"
                "You've seen that pattern before. "
                "Tonight. Somewhere.\n\n"
                "You can't place it yet."
            )
        return (
            "The cracked display case. "
            "Pre-Columbian ritual objects, purpose unknown. "
            "The crack runs diagonally — Danny's doing, probably.\n\n"
            "The geometric markings on the bowl still bother you. "
            "You still can't place why."
        )


cracked_case = _CrackedCase(
    name="display case",
    aliases=["case", "cracked case", "glass case", "ritual objects",
             "pre-columbian", "figurines", "obsidian", "bowl",
             "cracked display"],
    description="A cracked display case holding pre-Columbian ritual objects.",
    takeable=False,
)


# ---------------------------------------------------------------------------
# SARCOPHAGUS
# ---------------------------------------------------------------------------

class _Sarcophagus(Item):
    def on_examine(self, state):
        visits = getattr(state, 'sarcophagus_visits', 0)
        state.sarcophagus_visits = visits + 1
        if visits == 0:
            return (
                "An Egyptian sarcophagus, upright in its display alcove, "
                "behind a thick pane of preservation glass. "
                "Painted in the formal style — "
                "gold and lapis and the deep red of dried blood, "
                "hieroglyphs running in careful columns "
                "from the headdress to the feet.\n\n"
                "The placard: "
                "COFFIN OF UNKNOWN PROVENANCE. "
                "LATE PERIOD, CIRCA 600 BCE. "
                "ACQUIRED 1923. MISKATONIC ANTARCTIC EXPEDITION.\n\n"
                "You read that again.\n\n"
                "Antarctic.\n\n"
                "An Egyptian sarcophagus acquired on an Antarctic expedition. "
                "You let that sit for a moment.\n\n"
                "Behind the glass, behind the painted face, "
                "the mummy is visible — or the shape of it, "
                "the wrapped linen figure standing upright "
                "in the dark of its case.\n\n"
                "You have the distinct impression that it is facing forward. "
                "It has always been facing forward.\n\n"
                "You move on."
            )
        elif visits == 1:
            return (
                "The sarcophagus. The mummy behind its glass.\n\n"
                "Still facing forward.\n\n"
                "You don't know why you checked."
            )
        else:
            act = getattr(state, 'act', 1)
            if act >= 2:
                return (
                    "The sarcophagus.\n\n"
                    "The mummy is still there.\n\n"
                    "It is still facing forward.\n\n"
                    "The linen wrappings around its hands "
                    "look — looser than before.\n\n"
                    "You leave."
                )
            return (
                "The sarcophagus. The mummy. Forward-facing. "
                "You've confirmed this three times now. "
                "You're done confirming it."
            )


sarcophagus = _Sarcophagus(
    name="sarcophagus",
    aliases=["mummy", "egyptian", "coffin", "egyptian coffin",
             "mummy case", "linen", "wrapped figure"],
    description="An upright Egyptian sarcophagus behind preservation glass.",
    takeable=False,
)


# ---------------------------------------------------------------------------
# WORLD MAP
# ---------------------------------------------------------------------------

world_map = Item(
    name="world map",
    aliases=["map", "ancient map", "map of the ancient world",
             "wall map", "historical map"],
    description=(
        "A large printed reproduction of an ancient world map "
        "mounted behind perspex on the north wall — "
        "the Ptolemaic projection, roughly 150 CE, "
        "the world stretched and compressed into something "
        "that is recognizably earth but dreamily, wrongly proportioned.\n\n"
        "The Mediterranean is enormous. "
        "The British Isles are barely a rumor. "
        "Beyond the edges of the known world, "
        "the cartographer has written: HERE BE.\n\n"
        "Not HERE BE DRAGONS. Just HERE BE.\n\n"
        "You stare at that for longer than you mean to.\n\n"
        "HERE BE.\n\n"
        "Yeah."
    ),
    takeable=False,
)


# ---------------------------------------------------------------------------
# DIORAMAS
# ---------------------------------------------------------------------------

class _Dioramas(Item):
    def on_examine(self, state):
        visits = getattr(state, 'diorama_visits', 0)
        state.diorama_visits = visits + 1
        if visits == 0:
            return (
                "Three large diorama displays occupy the south wall, "
                "each depicting a scene from ancient life behind glass:\n\n"
                "LEFT: A Mesopotamian market scene — "
                "clay figurines at stalls, a ziggurat in the background. "
                "Detailed. Impressive. "
                "The figures are all facing the same direction.\n\n"
                "CENTER: An Egyptian burial preparation scene — "
                "priests around a central figure on a stone table. "
                "The lighting in the diorama makes the shadows long.\n\n"
                "RIGHT: A Pacific Island ritual scene — "
                "figures in a circle, a central fire, "
                "dense jungle behind them rendered in careful miniature.\n\n"
                "In the right diorama, one figure at the back of the circle "
                "is facing outward instead of inward. "
                "Facing the glass.\n\n"
                "Facing you.\n\n"
                "It's probably just how it was placed. "
                "These things happen in dioramas. "
                "Someone didn't check.\n\n"
                "You don't go back to that one."
            )
        elif visits == 1:
            return (
                "The three dioramas. "
                "Mesopotamia, Egypt, Pacific Islands.\n\n"
                "You don't look at the third one."
            )
        else:
            act = getattr(state, 'act', 1)
            if act >= 2:
                return (
                    "You look at the third diorama.\n\n"
                    "You told yourself you wouldn't.\n\n"
                    "The figure at the back of the circle "
                    "is still facing outward.\n\n"
                    "There are two of them now."
                )
            return (
                "Three dioramas. "
                "You're not looking at the third one. "
                "This is a decision you're comfortable with."
            )


dioramas = _Dioramas(
    name="dioramas",
    aliases=["diorama", "scenes", "display scenes", "ancient scenes",
             "mesopotamia", "egypt diorama", "pacific", "figures",
             "figurines", "third diorama", "pacific diorama"],
    description="Three large diorama displays of ancient life scenes.",
    takeable=False,
)


# ---------------------------------------------------------------------------
# ROPE / STANCHION
# ---------------------------------------------------------------------------

rope = Item(
    name="rope",
    aliases=["stanchion", "yellow tape", "tape", "barrier",
             "velvet rope", "do not cross"],
    description=(
        "Plastic stanchions connected by a length of yellow tape — "
        "the kind used for crowd control and, apparently, "
        "for cordoning off ancient artifacts of uncertain provenance.\n\n"
        "The handwritten sign dangling from it: DO NOT TOUCH — K\n\n"
        "Karen's handwriting. That same small, certain script.\n\n"
        "The tape has been broken and re-tied at one point. "
        "Danny didn't even put it back right."
    ),
    takeable=False,
)


# ---------------------------------------------------------------------------
# PLACARD (general hall placard)
# ---------------------------------------------------------------------------

placard = Item(
    name="placard",
    aliases=["placards", "sign", "information sign", "hall placard",
             "exhibit sign", "wall text"],
    description=(
        "A mounted information panel near the hall entrance:\n\n"
        "HALL OF ANCIENT CIVILIZATIONS\n\n"
        "This hall presents artifacts and reconstructions from "
        "civilizations spanning six thousand years of human history — "
        "from the earliest Mesopotamian city-states through "
        "the classical Mediterranean world and beyond.\n\n"
        "The Miskatonic Museum thanks the Hargrove Foundation "
        "for their generous support of this exhibition.\n\n"
        "Current acquisitions are being processed and will be "
        "added to the permanent collection pending authentication.\n\n"
        "You look at that last line.\n\n"
        "Pending authentication.\n\n"
        "The crate is pending authentication.\n\n"
        "You hope authentication takes a while."
    ),
    takeable=False,
)


# ---------------------------------------------------------------------------
# ROOM STRINGS
# ---------------------------------------------------------------------------

HALL_LONG = (
    "HALL OF ANCIENT CIVILIZATIONS\n\n"
    "The hall is long and high-ceilinged, the kind of space "
    "designed to make visitors feel the weight of history. "
    "At night, with the overhead lights off and only the "
    "emergency strips running along the baseboards, "
    "it mostly succeeds at making you feel small.\n\n"
    "Display cases line the walls — Egypt, Mesopotamia, "
    "pre-Columbian Americas, the Pacific Islands. "
    "One of the cases on the east wall is cracked. "
    "An upright sarcophagus stands in its alcove behind preservation glass, "
    "its painted face catching the emergency light.\n\n"
    "Three large dioramas occupy the south wall. "
    "Don't look too long at the third one.\n\n"
    "A large map of the ancient world covers the north wall.\n\n"
    "In the center of the hall, roped off with yellow tape "
    "and stanchions, a large open shipping crate. "
    "The lid has been set aside. "
    "Something pale lies on the floor a few feet away.\n\n"
    "There is a torn scrap of paper near the crate."
)

HALL_SHORT = (
    "HALL OF ANCIENT CIVILIZATIONS\n\n"
    "The long hall. The display cases. The crate, open and waiting. "
    "The pale thing on the floor."
)

HALL_AMBIENT = [
    "The emergency lighting gives everything in the hall "
    "the color of old photographs.",

    "One of the diorama figures casts a long shadow "
    "across the floor. You know which one.",

    "The sarcophagus stands in its alcove. "
    "You don't look at it directly. "
    "This is a habit you've developed in the last ten minutes.",

    "The crate sits in the center of the hall "
    "with the patient quality of something that has waited "
    "a very long time and is fine with waiting a little longer.",

    "Somewhere in this building, Danny is sitting in a corner "
    "holding a manuscript he should never have opened. "
    "You don't know that yet. "
    "You feel it anyway.",

    "The pale mask on the floor catches the emergency light. "
    "You look at it. "
    "You look at something else.",

    "The hieroglyphs on the sarcophagus run in careful columns. "
    "In your peripheral vision, they seem to rearrange themselves. "
    "Head-on, they're perfectly still.",
]


# ---------------------------------------------------------------------------
# FACTORY
# ---------------------------------------------------------------------------

def make_hall_of_civilizations():
    room = Room(
        name="Hall of Ancient Civilizations",
        short_desc=HALL_SHORT,
        long_desc=HALL_LONG,
        exits={
            "east": None,    # Gift Shop — wired in main.py
            "west": None,    # Natural History Wing — wired when built
        },
    )

    room.ambient_messages = HALL_AMBIENT

    room.items = [
        crate,
        pallid_mask,
        manuscript_fragment,
        cracked_case,
        sarcophagus,
        world_map,
        dioramas,
        rope,
        placard,
    ]

    return room
