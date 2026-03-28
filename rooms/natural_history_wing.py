# rooms/natural_history_wing.py
# Room 5: Natural History Wing
# Where things get properly wrong.
# Danny is here. The whale growls. The terminal knows your name.

from room import Room
from items import Item, ConsumableItem


# ---------------------------------------------------------------------------
# DANNY STATE
# Tracked on the room object: room.danny_present, room.danny_found
# Danny disappears if Nick leaves AND move count > danny_leave_threshold
# ---------------------------------------------------------------------------

DANNY_WHISPERS = [
    "\"...along the shore the cloud waves break...\"",
    "\"...the black stars rise...\"",
    "\"...Carcosa...\"",
    "\"...you, sir, should unmask...\"",
    "\"...has it begun already...\"",
    "\"...strange is the night where black stars rise...\"",
    "\"...the King in Yellow...\"",
    "\"...in the court of the dragon...\"",
    "\"...let the red dawn surmise...\"",
    "\"...it is a fearful thing...\"",
]

DANNY_EXAMINE_TEXTS = [
    # First look
    (
        "He's in the janitor's closet.\n\n"
        "Sitting upright, back against the rear wall, "
        "legs straight out in front of him like a child "
        "put in time-out by something vast and indifferent.\n\n"
        "Danny Gutierrez, your coworker. "
        "Sloppy Danny. Logbook Danny. All-good Danny.\n\n"
        "His hair is white. Not grey — white, "
        "the white of something that was never meant to change this fast. "
        "His eyes are open and aimed at the middle distance "
        "approximately six inches in front of his face.\n\n"
        "His lips are moving.\n\n"
        "\"...along the shore the cloud waves break...\"\n\n"
        "His right hand is closed around something. "
        "A key, you think. A key on a yellow lanyard.\n\n"
        "\"Danny.\"\n\n"
        "He doesn't respond.\n\n"
        "\"Danny, it's Nick.\"\n\n"
        "\"...the black stars rise...\"\n\n"
        "He's gone. Whatever is sitting here wearing Danny's uniform "
        "and Danny's face, it isn't Danny anymore."
    ),
    # Second look
    (
        "He's still here. Still upright. Still aimed at nothing.\n\n"
        "\"...Carcosa...\"\n\n"
        "His hand is still closed around the key.\n\n"
        "You study his face for a moment. "
        "You worked alongside this man for a week. "
        "He said 'sup' to you every night. "
        "He recommended the vending machine down the hall "
        "with the specific warning that it would eat your dollar.\n\n"
        "He was right about that.\n\n"
        "\"Sup, Danny.\"\n\n"
        "Nothing.\n\n"
        "\"...you, sir, should unmask...\"\n\n"
        "You stand there for a moment longer than you need to."
    ),
    # Third+ look
    (
        "Danny, white-haired, staring at nothing, "
        "whispering things he shouldn't know.\n\n"
        "\"...has it begun already...\"\n\n"
        "You stop looking. It doesn't help."
    ),
]

DANNY_SPRINT_TEXT = (
    "A figure sprints through the far end of the hall.\n\n"
    "White hair. Security uniform. Moving fast — "
    "faster than Danny has ever moved in his life, "
    "faster than a man in that condition should be able to move.\n\n"
    "He doesn't look at you.\n\n"
    "He runs through the Natural History Wing toward the lobby "
    "without slowing, without acknowledging the exhibits, "
    "without acknowledging anything.\n\n"
    "The sound of his footsteps recedes.\n\n"
    "Toward the front doors.\n\n"
    "The front doors that are chained shut.\n\n"
    "You don't hear him stop."
)

DANNY_GONE_TEXT = (
    "The janitor's closet is empty.\n\n"
    "The light is still on. "
    "The muttering has stopped.\n\n"
    "On the floor where Danny was sitting: "
    "a small rectangle of worn fabric, "
    "dark at the edges. "
    "His name tag. GUTIERREZ.\n\n"
    "Still warm."
)


# ---------------------------------------------------------------------------
# JANITOR'S CLOSET
# ---------------------------------------------------------------------------

class _JanitorCloset(Item):
    def on_examine(self, state):
        if getattr(state, 'danny_gone', False):
            return DANNY_GONE_TEXT
        return (
            "A utility door set into the west wall, "
            "MAINTENANCE stenciled on it in faded letters.\n\n"
            "Light seeps under the door. "
            "Amber, warm, inconsistent — "
            "like something is moving in front of it.\n\n"
            "And a sound. Low. Continuous. "
            "The sound of someone talking to themselves "
            "in a voice that has given up on being heard.\n\n"
            "You stand at the door for a moment.\n\n"
            "You knock.\n\n"
            "The muttering doesn't stop."
        )

    def on_open(self, state):
        return self.on_examine(state)

    def on_use(self, state):
        return self.on_examine(state)


janitor_closet = _JanitorCloset(
    name="janitor's closet",
    aliases=["closet", "maintenance door", "utility door", "door",
             "janitor closet", "maintenance closet", "light under door"],
    description="A maintenance door with light seeping under it and muttering within.",
    takeable=False,
)


# ---------------------------------------------------------------------------
# DANNY (interactable presence)
# ---------------------------------------------------------------------------

class _Danny(Item):
    def on_examine(self, state):
        if getattr(state, 'danny_gone', False):
            return DANNY_GONE_TEXT
        visits = getattr(state, 'danny_examine_count', 0)
        state.danny_examine_count = visits + 1
        idx = min(visits, len(DANNY_EXAMINE_TEXTS) - 1)
        state.danny_found = True
        state.act = 2
        return DANNY_EXAMINE_TEXTS[idx]

    def on_take(self, state):
        return (
            "You can't take Danny. "
            "You could theoretically drag him, "
            "but you suspect he'd whisper the whole time "
            "and that would be worse."
        )

    def on_use(self, state):
        return self.on_examine(state)


danny = _Danny(
    name="danny",
    aliases=["gutierrez", "danny gutierrez", "coworker",
             "security guard", "him", "the man"],
    description="Danny Gutierrez. Your coworker. Not anymore.",
    takeable=False,
)


# ---------------------------------------------------------------------------
# DANNY'S KEY
# ---------------------------------------------------------------------------

class _DannyKey(Item):
    def on_examine(self, state):
        if self.taken:
            return (
                "A standard museum master key on a yellow lanyard. "
                "STAFF ONLY stamped on the fob.\n\n"
                "It opens the sub-basement access door. "
                "You know this because you tried it on the way past "
                "and the lock turned and you kept walking "
                "and now you know where you're not ready to go yet."
            )
        if getattr(state, 'danny_gone', False):
            return "Danny's gone. The key went with him."
        return (
            "A key on a yellow lanyard, "
            "visible in Danny's closed right hand.\n\n"
            "STAFF ONLY stamped on the fob.\n\n"
            "The lanyard is yellow. "
            "The same yellow as the ornament. "
            "The same yellow as the can in the vending machine.\n\n"
            "You're going to need that key."
        )

    def on_take(self, state):
        if self.taken:
            return "You already have it."
        if getattr(state, 'danny_gone', False):
            return "Danny's gone. The key went with him."
        self.taken = True
        state.danny_key_taken = True
        return (
            "You reach down and try to uncurl Danny's fingers.\n\n"
            "His grip is stronger than it should be. "
            "Much stronger. "
            "You pull anyway.\n\n"
            "He bites you.\n\n"
            "Not hard — not breaking-skin hard — "
            "but with the specific focused intent "
            "of something that has one remaining directive "
            "and that directive is hold the key.\n\n"
            "You pull harder. His fingers open. "
            "The key comes free.\n\n"
            "Danny's hand closes again, "
            "curling around nothing, "
            "maintaining the grip on something that isn't there anymore.\n\n"
            "\"...the King in Yellow...\"\n\n"
            "Your hand is shaking slightly. "
            "Not from the bite.\n\n"
            "You have the key."
        )


danny_key = _DannyKey(
    name="danny's key",
    aliases=["key", "yellow lanyard", "lanyard", "staff key",
             "sub-basement key", "master key", "danny key"],
    description="A museum key on a yellow lanyard, gripped in Danny's hand.",
    takeable=True,
)


# ---------------------------------------------------------------------------
# WHALE MODEL
# ---------------------------------------------------------------------------

class _WhaleModel(Item):
    def on_examine(self, state):
        visits = getattr(state, 'whale_model_visits', 0)
        state.whale_model_visits = visits + 1

        if visits == 0:
            return (
                "A full-scale fiberglass replica of a blue whale, "
                "suspended from the ceiling on thick steel cables. "
                "Painted in that particular shade of blue that tries "
                "to approximate the real thing and doesn't quite.\n\n"
                "It's large. Obviously large — you knew it would be large. "
                "You've seen the skeleton in the lobby. "
                "But the model is different. "
                "The model has mass. Presence. Paint.\n\n"
                "The model has teeth.\n\n"
                "You look at the teeth for a moment.\n\n"
                "You think about Margaret in the lobby.\n\n"
                "You decide not to think about Margaret in the lobby.\n\n"
                "The whale hangs overhead, patient and enormous "
                "and absolutely not moving.\n\n"
                "Absolutely not."
            )
        elif visits == 1:
            return (
                "You look up at the whale model.\n\n"
                "It is a fiberglass replica. "
                "It cannot move. "
                "It does not have a respiratory system. "
                "It cannot produce sound.\n\n"
                "You heard what you heard.\n\n"
                "You look at something else."
            )
        else:
            act = getattr(state, 'act', 1)
            if act >= 2:
                return (
                    "The whale model hangs overhead.\n\n"
                    "You don't look at it directly. "
                    "This is a choice you've made and you're comfortable with it."
                )
            return (
                "The whale model. Fiberglass. Painted. "
                "Hanging. "
                "Not moving.\n\n"
                "The teeth are still there."
            )


whale_model = _WhaleModel(
    name="whale model",
    aliases=["whale", "fiberglass whale", "model whale", "replica whale",
             "blue whale", "ceiling whale", "the whale"],
    description="A full-scale fiberglass blue whale replica suspended from the ceiling.",
    takeable=False,
)

WHALE_GROWL_TEXT = (
    "The whale model hangs overhead.\n\n"
    "And then —\n\n"
    "A sound.\n\n"
    "Low. Sustained. "
    "Coming from the direction of the ceiling, "
    "from the direction of forty feet of painted fiberglass "
    "that cannot, under any circumstances, produce sound.\n\n"
    "It is a growl.\n\n"
    "It lasts for approximately three seconds.\n\n"
    "It stops.\n\n"
    "The Natural History Wing is very quiet.\n\n"
    "You look up at the whale.\n\n"
    "The whale does not look back.\n\n"
    "You decide to believe that."
)


# ---------------------------------------------------------------------------
# INFORMATION TERMINAL
# ---------------------------------------------------------------------------

class _InfoTerminal(Item):
    def on_examine(self, state):
        visits = getattr(state, 'terminal_visits', 0)
        state.terminal_visits = visits + 1

        if visits == 0:
            return (
                "A touchscreen information kiosk near the entrance — "
                "the kind that's supposed to show exhibit information "
                "and museum maps and be off after closing.\n\n"
                "It's on.\n\n"
                "The screen shows a staff login page. "
                "Someone is already logged in.\n\n"
                "Username: D.GUTIERREZ\n\n"
                "Last search query, still visible in the search bar:\n\n"
                "   king yellow mask manuscript provenance\n\n"
                "Timestamp: 11:34 PM.\n\n"
                "An hour ago. Danny knew what he was looking for "
                "before he opened the crate.\n\n"
                "You touch the screen to clear it.\n\n"
                "It doesn't clear.\n\n"
                "The search results load instead."
            )
        elif visits == 1:
            return _terminal_glitch_1(state)
        elif visits == 2:
            return _terminal_glitch_2(state)
        else:
            return (
                "The screen is cracked now. "
                "From the inside.\n\n"
                "You're not touching it again."
            )

    def on_use(self, state):
        return self.on_examine(state)

    def on_read(self, state):
        return self.on_examine(state)


def _terminal_glitch_1(state):
    return (
        "The screen flickers.\n\n"
        "Static. The kind of static that comes from "
        "interference, from bad signal, from things "
        "broadcasting on frequencies they shouldn't.\n\n"
        "Then it resolves.\n\n"
        "It's a video.\n\n"
        "The quality is wrong — too sharp in some places, "
        "smeared in others, like something that was filmed "
        "in a place where light doesn't behave.\n\n"
        "You recognize the woman on screen immediately.\n\n"
        "Jennifer.\n\n"
        "Your ex-wife. Her face. Her voice. "
        "But something behind the eyes is wrong — "
        "they're too dark, too still, "
        "the eyes of something wearing Jennifer's face "
        "and not quite understanding how eyes are supposed to work.\n\n"
        "She speaks.\n\n"
        "\"You knew she was sick, Nick. "
        "You knew for months. "
        "You chose the job. You chose the hours. "
        "You chose everything except the one thing that mattered.\"\n\n"
        "Her voice is Jennifer's voice. "
        "The cadence. The specific way she says your name.\n\n"
        "\"Avery asked for you. At the end. "
        "Did you know that? "
        "She asked for you and you weren't there.\"\n\n"
        "You stand in front of the kiosk screen "
        "in the Natural History Wing of the Miskatonic Museum "
        "at 12:47 AM on December 20th "
        "and you don't move and you don't speak "
        "and something that is wearing your ex-wife's face "
        "says every true thing you've been carrying "
        "since the hospital.\n\n"
        "You cry.\n\n"
        "You don't make a sound. "
        "Just your face, in the dark, in the emergency lighting. "
        "Just that.\n\n"
        "The screen goes to static.\n\n"
        "Then off.\n\n"
        "Then on again."
    )


def _terminal_glitch_2(state):
    return (
        "The screen shows a camera feed.\n\n"
        "You recognize the angle immediately — "
        "the Main Lobby, from above, "
        "from a camera you couldn't identify earlier. "
        "Channel 12. The one that wasn't on your monitors.\n\n"
        "The timestamp in the corner reads: 11:06 PM.\n\n"
        "An hour ago. The lobby.\n\n"
        "You are in the frame.\n\n"
        "You — smaller than you expect yourself to look, "
        "standing near the information desk — "
        "and Maya, by the staff exit, coat on, "
        "laughing at something you said.\n\n"
        "You watch yourself talk to Maya "
        "for approximately forty seconds.\n\n"
        "It was a good forty seconds.\n\n"
        "Then the camera feed does something "
        "camera feeds are not supposed to do.\n\n"
        "It zooms.\n\n"
        "Not mechanically — "
        "not the smooth zoom of a PTZ camera — "
        "but the way a living thing leans in. "
        "Interested. Hungry.\n\n"
        "It zooms in on your face.\n\n"
        "And stops.\n\n"
        "The screen cracks from the inside. "
        "A single fracture line, "
        "running from the center outward, "
        "like something pressed against it from the other side.\n\n"
        "You step back.\n\n"
        "You are done with this terminal."
    )


info_terminal = _InfoTerminal(
    name="information terminal",
    aliases=["terminal", "kiosk", "screen", "touchscreen",
             "info kiosk", "computer", "monitor kiosk",
             "information kiosk", "info terminal", "info"],
    description="A staff information kiosk. It should be off. It isn't.",
    takeable=False,
)


# ---------------------------------------------------------------------------
# VENDING MACHINE
# ---------------------------------------------------------------------------

class _VendingMachine(Item):
    def on_examine(self, state):
        return (
            "The vending machine Danny mentioned in the logbook — "
            "the one that ate his dollar.\n\n"
            "It's a standard museum snack machine: "
            "chips, granola bars, overpriced candy. "
            "Most of the slots are empty.\n\n"
            "In the bottom dispenser slot, "
            "a single can that wasn't vended — "
            "just sitting there, waiting.\n\n"
            "The can has no label except for a symbol "
            "pressed into the metal. "
            "Yellow. Angular. Recursive.\n\n"
            "You've seen that symbol before tonight.\n\n"
            "The can feels full."
        )

    def on_use(self, state):
        return self.on_examine(state)


class _YellowCan(Item):
    def on_examine(self, state):
        if getattr(state, 'can_thrown', False):
            return (
                "The yellow can is across the room where you threw it. "
                "It didn't open when it hit the wall. "
                "It didn't dent.\n\n"
                "You leave it there."
            )
        return (
            "The can with no label. "
            "Just the yellow symbol pressed into the metal.\n\n"
            "It feels full when you hold it. "
            "Heavier than a can should be.\n\n"
            "Cold.\n\n"
            "Always cold."
        )

    def on_eat(self, state):
        return self.on_drink(state)

    def on_drink(self, state):
        if getattr(state, 'can_thrown', False):
            return "It's across the room. You're not going back for it."
        if getattr(state, 'can_attempted', False):
            # Second attempt — the burn
            state.can_thrown = True
            self.taken = False
            return (
                "You try again.\n\n"
                "The moment the opening touches your lips "
                "something happens that isn't heat exactly — "
                "more like the memory of heat, "
                "like touching something that burned "
                "a long time ago in a dream.\n\n"
                "Your hand throws the can across the room "
                "before you've made the decision to throw it.\n\n"
                "Purely reflexive. "
                "Your body making a better decision than your brain.\n\n"
                "The can hits the far wall. "
                "Doesn't open. Doesn't dent. "
                "Sits where it landed.\n\n"
                "Nothing came out of it.\n\n"
                "Nothing was ever going to come out of it."
            )
        state.can_attempted = True
        return (
            "You pull the tab.\n\n"
            "Nothing comes out.\n\n"
            "You tip it. Nothing. "
            "You look inside the opening. "
            "Dark.\n\n"
            "The can still feels full.\n\n"
            "You lower it slowly."
        )

    def on_take(self, state):
        if getattr(state, 'can_thrown', False):
            return "It's across the room. You leave it."
        self.taken = True
        return (
            "You take the can from the dispenser slot.\n\n"
            "It's heavier than it should be "
            "and colder than the machine could account for.\n\n"
            "The symbol on the side catches the emergency lighting.\n\n"
            "You put it in your jacket pocket next to the mask."
        )


vending_machine = _VendingMachine(
    name="vending machine",
    aliases=["machine", "snack machine", "vending", "snacks"],
    description="A mostly-empty vending machine with one can in the dispenser slot.",
    takeable=False,
)

yellow_can = _YellowCan(
    name="yellow can",
    aliases=["can", "yellow can", "unlabeled can", "strange can",
             "symbol can", "the can"],
    description="A can with no label — just a yellow symbol pressed into the metal.",
    takeable=True,
)


# ---------------------------------------------------------------------------
# T-REX SKELETON
# ---------------------------------------------------------------------------

class _TRex(Item):
    def on_examine(self, state):
        visits = getattr(state, 'trex_visits', 0)
        state.trex_visits = visits + 1
        if visits == 0:
            return (
                "A Tyrannosaurus Rex skeleton, mounted on a steel armature "
                "in a mid-stride pose, head lowered, "
                "occupying the center of the hall with the authority "
                "of something that was the apex predator "
                "of its entire geological era.\n\n"
                "It is the largest thing in this room.\n\n"
                "It is currently the second most frightening.\n\n"
                "Danny is sitting at its base, "
                "back against the pedestal, "
                "aimed at nothing.\n\n"
                "You look up at sixty-five-million-year-old teeth "
                "and then down at your coworker "
                "and you're not sure which direction "
                "has the worse thing in it right now."
            )
        return (
            "The T-Rex skeleton. "
            "Danny at its base.\n\n"
            "Sixty-five million years of predator "
            "and one man who opened a crate he shouldn't have.\n\n"
            "You don't know which one you feel worse for."
        )


trex = _TRex(
    name="t-rex",
    aliases=["tyrannosaurus", "dinosaur", "rex", "skeleton",
             "t rex", "trex", "dinosaur skeleton", "tyrannosaur"],
    description="A mounted T-Rex skeleton, dominant in the center of the hall.",
    takeable=False,
)


# ---------------------------------------------------------------------------
# MOSASAUR SKELETON (wall mount)
# ---------------------------------------------------------------------------

class _Mosasaur(Item):
    def on_examine(self, state):
        visits = getattr(state, 'mosasaur_visits', 0)
        state.mosasaur_visits = visits + 1
        if visits == 0:
            return (
                "A mosasaur skeleton mounted on the east wall — "
                "a marine reptile, roughly forty feet long, "
                "the placard placing it at 70 million years old.\n\n"
                "It looks like what would happen if a crocodile "
                "decided the ocean wasn't dangerous enough.\n\n"
                "The jaws are open. They are always open — "
                "that's how mounted specimens work, "
                "you know this — "
                "but at this angle, in this light, "
                "they look less like a display pose "
                "and more like something interrupted mid-action.\n\n"
                "You think one of the ribs moved.\n\n"
                "It didn't."
            )
        act = getattr(state, 'act', 1)
        if act >= 2:
            return (
                "The mosasaur skeleton on the wall.\n\n"
                "You thought you saw a rib move before.\n\n"
                "You look at it carefully.\n\n"
                "Two ribs are in different positions than they were.\n\n"
                "You walk away quickly."
            )
        return (
            "The mosasaur skeleton. Forty feet of marine predator "
            "on the east wall.\n\n"
            "Jaws open. Ribs still. "
            "You check."
        )


mosasaur = _Mosasaur(
    name="mosasaur",
    aliases=["mosasaur skeleton", "marine reptile", "sea reptile",
             "wall skeleton", "lizard skeleton", "sea monster"],
    description="A massive mosasaur skeleton mounted on the east wall.",
    takeable=False,
)


# ---------------------------------------------------------------------------
# SKULL DISPLAY
# ---------------------------------------------------------------------------

class _SkullDisplay(Item):
    def on_examine(self, state):
        visits = getattr(state, 'skull_visits', 0)
        state.skull_visits = visits + 1
        if visits == 0:
            return (
                "A low display case running along the north wall: "
                "the evolution of the human skull, "
                "arranged left to right across four million years.\n\n"
                "Australopithecus. Homo habilis. "
                "Homo erectus. Homo sapiens.\n\n"
                "The progression is familiar — "
                "you've seen this in textbooks, in museums, "
                "in the background of documentaries.\n\n"
                "There is a fifth skull.\n\n"
                "At the far right end of the case, "
                "past homo sapiens, "
                "past the implied endpoint of the sequence.\n\n"
                "It has no placard.\n\n"
                "The shape is wrong in ways "
                "you can't immediately articulate — "
                "the cranium is too large, "
                "the orbital structure subtly off, "
                "the overall geometry suggesting "
                "a head that was designed to think "
                "about things your head wasn't.\n\n"
                "There is no placard because "
                "there is no name for what this is.\n\n"
                "You look at it for a long time.\n\n"
                "You look away.\n\n"
                "You look back.\n\n"
                "It has not moved.\n\n"
                "This is the most reassuring thing "
                "that has happened to you tonight."
            )
        return (
            "The skull display. "
            "Four million years of human evolution "
            "and then whatever that fifth one is.\n\n"
            "Still no placard.\n\n"
            "Still the wrong shape.\n\n"
            "Still not moving."
        )


skull_display = _SkullDisplay(
    name="skull display",
    aliases=["skulls", "skull", "display case", "evolution display",
             "human skulls", "fifth skull", "unknown skull",
             "skull case", "evolution"],
    description="A display of human skull evolution — with one extra at the end.",
    takeable=False,
)


# ---------------------------------------------------------------------------
# ICE AGE DIORAMA / PREHISTORIC DISPLAYS
# ---------------------------------------------------------------------------

class _PrehistoricDioramas(Item):
    def on_examine(self, state):
        visits = getattr(state, 'prehistoric_visits', 0)
        state.prehistoric_visits = visits + 1
        if visits == 0:
            return (
                "Several large prehistoric dioramas line the south wall:\n\n"
                "A woolly mammoth scene — a family group "
                "moving across a painted tundra, "
                "rendered in impressive detail. "
                "The mammoths' eyes catch the emergency lighting "
                "in a way that makes them look wet. "
                "Alive.\n\n"
                "A cave scene — early humans around a fire, "
                "cave paintings visible on the walls behind them. "
                "The paintings are accurate to the period. "
                "You look at them for a moment.\n\n"
                "The paintings on the cave wall in the diorama "
                "include one that doesn't belong. "
                "It's in the back, half-shadowed. "
                "A symbol. Angular. Recursive.\n\n"
                "You have seen that symbol three times tonight.\n\n"
                "A megalodon display — the massive shark jaw "
                "open wide enough to stand inside, "
                "with a small information plaque: "
                "CARCHAROCLES MEGALODON. EXTINCT 3.6 MILLION YEARS AGO.\n\n"
                "You look at the jaw.\n\n"
                "You look at the whale model overhead.\n\n"
                "You move on."
            )
        act = getattr(state, 'act', 1)
        if act >= 2:
            return (
                "The prehistoric dioramas.\n\n"
                "The mammoth eyes are still wet-looking.\n\n"
                "The cave painting with the symbol — "
                "it's larger than it was. "
                "Or you're standing closer. "
                "One of those.\n\n"
                "You walk past without stopping."
            )
        return (
            "The woolly mammoths, the cave scene, the megalodon jaw.\n\n"
            "The symbol in the cave painting. "
            "You've stopped counting how many times you've seen it."
        )


prehistoric_dioramas = _PrehistoricDioramas(
    name="dioramas",
    aliases=["prehistoric dioramas", "mammoth", "woolly mammoth",
             "cave scene", "cave painting", "megalodon", "shark jaw",
             "displays", "prehistoric displays", "diorama"],
    description="Prehistoric dioramas including mammoth, cave, and megalodon displays.",
    takeable=False,
)


# ---------------------------------------------------------------------------
# FOSSIL DISPLAY
# ---------------------------------------------------------------------------

fossil_display = Item(
    name="fossil display",
    aliases=["fossils", "ammonites", "trilobites", "fossil case",
             "ancient fossils", "fossil"],
    description=(
        "A long case of fossil specimens — "
        "ammonites, trilobites, ancient sea creatures "
        "from the Cambrian and Devonian periods.\n\n"
        "The placards list dates. "
        "You read them.\n\n"
        "500 million years. "
        "450 million years. "
        "380 million years.\n\n"
        "You do the math without wanting to.\n\n"
        "Modern humans have existed for roughly 300,000 years. "
        "The museum itself is 90 years old. "
        "You have been alive for 38 years. "
        "You have worked here for 6 days.\n\n"
        "The trilobite in front of you "
        "existed for 270 million years "
        "before going extinct.\n\n"
        "You stand in the dark in a blizzard "
        "holding a flashlight and a radio "
        "and a key you took from a man who lost his mind "
        "and you feel very, very recent.\n\n"
        "And very temporary."
    ),
    takeable=False,
)


# ---------------------------------------------------------------------------
# EMERGENCY EXIT
# ---------------------------------------------------------------------------

emergency_exit = Item(
    name="emergency exit",
    aliases=["emergency door", "exit door", "alarmed door",
             "far door", "back door", "fire exit"],
    description=(
        "A heavy steel door at the far end of the wing, "
        "a red EXIT sign glowing above it.\n\n"
        "EMERGENCY EXIT — ALARM WILL SOUND\n\n"
        "Through the small reinforced window in the door: "
        "white. Just white. "
        "The blizzard has been working on this side of the building too.\n\n"
        "You could open it. "
        "The alarm would go off. "
        "You'd step into approximately two feet of snow "
        "with no coat, no car keys, "
        "and the nearest open business "
        "somewhere between here and impossible.\n\n"
        "You leave it closed.\n\n"
        "The blizzard doesn't mind."
    ),
    takeable=False,
)


# ---------------------------------------------------------------------------
# ROOM STRINGS
# ---------------------------------------------------------------------------

WING_LONG = (
    "NATURAL HISTORY WING\n\n"
    "The wing opens above you, high-ceilinged and wide, "
    "the kind of space that earns its square footage. "
    "A full-scale fiberglass whale hangs from the ceiling — "
    "painted blue, enormous, not the real thing "
    "but trying hard to be.\n\n"
    "Dinosaur skeletons. Prehistoric dioramas. "
    "A mosasaur on the east wall, jaws open. "
    "A long skull display along the north wall "
    "that ends with something that shouldn't be there.\n\n"
    "The information terminal near the entrance is on "
    "when it shouldn't be. "
    "The vending machine Danny mentioned still sits against the wall, "
    "a single unmarked can in the dispenser slot.\n\n"
    "A janitor's closet door is set into the west wall. "
    "Light seeps under it. "
    "Someone in there is talking.\n\n"
    "The emergency exit glows red at the far end.\n\n"
    "To the east: the Reading Room."
)

WING_SHORT = (
    "NATURAL HISTORY WING\n\n"
    "The whale overhead. The bones in the dark. "
    "The closet with the light under the door."
)

WING_AMBIENT = [
    "The whale model hangs overhead, enormous and still. "
    "You think about not thinking about the sound it made.",

    "The mammoth eyes in the diorama catch the emergency light. "
    "You look away. "
    "When you look back they're aimed somewhere else.",

    "The muttering from the janitor's closet "
    "rises and falls like a tide. "
    "\"...the black stars rise...\"\n"
    "You hear it even when you're not listening for it.",

    "The mosasaur skeleton on the wall. "
    "You glance at the ribs. "
    "You're not doing that anymore.",

    "Something in the prehistoric diorama moves. "
    "You look directly at it. "
    "Everything is still. "
    "You look away. "
    "You catch it in your peripheral vision. "
    "It stops.",

    "The fossil display catches your eye. "
    "500 million years of life on earth, "
    "and something managed to end most of it "
    "at least five times. "
    "You find this oddly comforting given current circumstances.",

    "The fifth skull at the end of the display case "
    "has no placard. "
    "You checked. "
    "You're going to check again in a minute. "
    "You already know what you're going to find.",
]


# ---------------------------------------------------------------------------
# FACTORY
# ---------------------------------------------------------------------------

def make_natural_history_wing():
    room = Room(
        name="Natural History Wing",
        short_desc=WING_SHORT,
        long_desc=WING_LONG,
        exits={
            "south": None,    # Hall of Civilizations — wired in main.py
            "east": None,     # Reading Room — wired when built
        },
    )

    room.ambient_messages = WING_AMBIENT

    # Room-level state
    room.danny_present = True
    room.danny_found = False
    room.whale_growl_fired = False
    room.danny_sprint_fired = False
    room.danny_moves = 0        # moves Nick has spent in this room

    room.items = [
        janitor_closet,
        danny,
        danny_key,
        whale_model,
        info_terminal,
        vending_machine,
        yellow_can,
        trex,
        mosasaur,
        skull_display,
        prehistoric_dioramas,
        fossil_display,
        emergency_exit,
    ]

    return room
