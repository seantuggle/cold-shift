#!/usr/bin/env python3
# main.py
# COLD SHIFT — main game loop
# Run this file to play.

import sys
import random
from parser import parse, DIRECTIONS
from player import Player
from engine.game_state import GameState

# Room imports
from rooms.security_office import (
    make_security_office,
    radio, telephone, logbook, postit, monitors, monitor_7,
    dannys_note, dannys_desk, corkboard, schedule,
    coffee, ramen, soda, sports_drink, hot_sauce,
    fridge, magazine, calendar, sock, stapler,
    plant, novelty_mug, lost_and_found, mirror, nicks_desk,
)

# ---------------------------------------------------------------------------
# WORLD SETUP
# ---------------------------------------------------------------------------

def build_world():
    """Create all rooms and wire up exits."""
    security_office = make_security_office()

    from rooms.main_lobby import make_main_lobby
    main_lobby = make_main_lobby()

    # Wire exits
    security_office.exits["north"] = main_lobby
    main_lobby.exits["south"] = security_office
    # East and West stubs — wired when those rooms are built
    # main_lobby.exits["east"] = gift_shop
    # main_lobby.exits["west"] = hall_of_antiquities

    return security_office, main_lobby   # return both for lobby access


# ---------------------------------------------------------------------------
# STARTING INVENTORY
# ---------------------------------------------------------------------------

JACKET_DESC = (
    "Your jacket. Canvas, worn at the elbows. Not warm enough for December, "
    "which is fine because you're inside, and if you were going outside "
    "you'd have bigger problems than the jacket.\n\n"
    "Breast pocket: security badge. NICK. At least they got the first name right.\n"
    "Right pocket: your cell phone.\n"
    "Left pocket: a pen and a stick of gum.\n"
    "On your belt: your keys.\n\n"
    "It hangs on its hook by the door like it's waiting for something to happen."
)

STARTING_ITEMS_DESC = {
    "cell phone": (
        "Your cell phone. Three bars — the blizzard is already eating "
        "the signal. A text from an unknown number, sent three days ago, "
        "that you haven't opened. You know who it's from. "
        "Two missed calls from your lawyer. Nothing else."
    ),
    "gum": (
        "A single stick of spearmint gum, slightly squashed "
        "from living in your jacket pocket. "
        "It's gum. It does what gum does."
    ),
    "keys": (
        "Your key ring. Museum master key — opens most staff doors. "
        "A smaller key you don't recognize. "
        "And your apartment key, which opens a door to a place "
        "that doesn't feel like home yet and might not for a while."
    ),
    "wallet": (
        "Brown leather, worn at the corners. "
        "Security badge ID. Twelve dollars in cash. "
        "A library card you keep meaning to use. "
        "Behind everything else, a photo you keep meaning to move "
        "but don't. You don't take it out."
    ),
    "flashlight": (
        "Standard-issue security flashlight. Heavy, reliable, "
        "the kind built to survive being dropped repeatedly "
        "by people who are paid not to care about it. "
        "Currently off."
    ),
}


# ---------------------------------------------------------------------------
# KAREN
# ---------------------------------------------------------------------------

KAREN_CALLS = [
    "\"Callahan.\" Just your name. Delivered like a verdict. "
    "You tell her all's quiet. \"It should be quiet. That's the job.\" "
    "Click.",

    "\"Callahan. East wing by midnight. Clear?\" "
    "You confirm. She's already gone.",

    "\"Callahan. Status.\" You update her. "
    "Silence. Then: \"Don't touch the crate.\" "
    "She hangs up before you can tell her you know.",

    "\"Callahan. Where's Gutierrez?\" "
    "You tell her you haven't seen Danny in a while. "
    "A pause. \"Find him.\" Click. "
    "Officious little— you let the thought go.",

    "\"Callahan. Report.\" You report. "
    "She says nothing for three full seconds and then hangs up. "
    "You stare at the radio. You wonder if she was born like this "
    "or if it took practice.",
]


def karen_interrupts(state):
    """Fire a Karen radio call if it's time."""
    if state.moves - state.last_karen_call >= state.KAREN_INTERVAL:
        state.last_karen_call = state.moves
        state.karen_calls += 1
        idx = min(state.karen_calls - 1, len(KAREN_CALLS) - 1)
        print("\n" + "─" * 50)
        print("[ RADIO CRACKLES ]")
        print(KAREN_CALLS[idx])
        print("─" * 50 + "\n")


# ---------------------------------------------------------------------------
# VERB HANDLERS
# ---------------------------------------------------------------------------

def handle_go(noun, player, state):
    if not noun or noun not in DIRECTIONS.values():
        return "Which direction?"
    direction = noun
    room = player.current_room
    if direction not in room.exits or room.exits[direction] is None:
        return "You can't go that way."
    player.current_room = room.exits[direction]
    return player.current_room.describe(state)


def handle_look(noun, player, state):
    if noun:
        return handle_examine(noun, player, state)
    return player.current_room.look(state)


def handle_examine(noun, player, state):
    if not noun:
        return handle_look(None, player, state)

    # Jacket
    if noun in ["jacket", "coat", "canvas jacket", "my jacket"]:
        return JACKET_DESC

    # Check inventory first
    item = player.get_item(noun)
    if item:
        return item.on_examine(state)

    # Check room
    item = player.current_room.find_item(noun)
    if item:
        return item.on_examine(state)

    # Special examine cases for starting inventory
    for key in STARTING_ITEMS_DESC:
        if noun in key or key in noun:
            return STARTING_ITEMS_DESC[key]

    # Room itself
    if noun in ["room", "here", "around", "surroundings", "office"]:
        return player.current_room.look(state)

    return f"You don't see any {noun} here."


def handle_take(noun, player, state):
    if not noun:
        return "Take what?"

    # Can't take things already in inventory
    if player.get_item(noun):
        return "You're already carrying that."

    item = player.current_room.find_item(noun)
    if not item:
        return f"You don't see any {noun} here."

    result = player.take(item, state)

    # Special radio logic
    if item == radio:
        state.radio_taken = True
        result += (
            "\n\nYou clip it to your belt. "
            "Karen's voice crackles immediately, as if she was waiting.\n"
            "\"Callahan. You should have had that on you from the start.\"\n"
            "Click."
        )

    return result


def handle_drop(noun, player, state):
    if not noun:
        return "Drop what?"
    item = player.get_item(noun)
    if not item:
        return f"You're not carrying any {noun}."
    return player.drop(item, state)


def handle_inventory(player):
    return player.inventory_list()


def handle_eat(noun, player, state):
    if not noun:
        return "Eat what?"
    # Check inventory first, then room
    item = player.get_item(noun) or player.current_room.find_item(noun)
    if not item:
        return f"You don't see any {noun} here."
    return item.on_eat(state)


def handle_drink(noun, player, state):
    return handle_eat(noun, player, state)


def handle_read(noun, player, state):
    if not noun:
        return "Read what?"

    item = player.get_item(noun) or player.current_room.find_item(noun)

    if not item:
        # Special: read post-it from inventory
        if "post" in noun or "untruths" in noun or "rears" in noun:
            return handle_postit_read(state)
        return f"You don't see any {noun} here."

    if item == logbook:
        return item.on_examine(state)

    if item == postit or item.matches("post-it"):
        return handle_postit_read(state)

    if item == schedule:
        return schedule.description

    if item == dannys_note:
        return dannys_note.description

    if item == magazine:
        return magazine.description

    if item == calendar:
        return calendar.description

    return f"There's nothing particularly illuminating to read on the {item.name}."


def handle_postit_read(state):
    if state.postit_reversed:
        return (
            "You look at it again.\n\n"
            "rears untruths.\n\n"
            "Hastur returns.\n\n"
            "You already know what it says. You put it back in your pocket "
            "and try not to say it out loud again."
        )
    return postit.description


def handle_reverse(noun, player, state):
    """Player tries to reverse/decode the post-it."""
    noun = (noun or "").lower()
    is_postit_target = (
        "post" in noun or "note" in noun or
        "untruths" in noun or "rears" in noun or
        not noun
    )
    if not is_postit_target:
        return "Reverse what?"
    # Auto-add postit to inventory if examined (examine text implies pocketing)
    if not player.has_item("post-it") and postit not in player.inventory:
        in_room = player.current_room.find_item("post-it")
        if not in_room and not player.has_item("post-it"):
            return (
                "You'd need the Post-it note to work that out. "
                "It's on the corkboard."
            )
    if state.postit_reversed:
        return (
            "You've already worked it out. You try not to think about "
            "what you said out loud when you did."
        )
    state.postit_reversed = True
    return (
        "You stare at the note.\n\n"
        "   rears untruths\n\n"
        "You mouth it backwards without really meaning to.\n\n"
        "Hastur returns.\n\n"
        "You sit with that for a moment.\n\n"
        "The radio static shifts frequency for exactly one second, "
        "then goes back to normal.\n\n"
        "You put the Post-it in your pocket and try not to think "
        "about what you just said out loud."
    )


def handle_write(noun, player, state):
    if "logbook" in (noun or "") or "log" in (noun or "") or not noun:
        if state.logbook_written:
            return (
                "You've already made tonight's entry. "
                "'All quiet. On patrol.' "
                "It still feels like a lie you haven't earned yet."
            )
        if not player.has_item("pen") and not player.has_item("jacket"):
            return "You need something to write with. Your pen is in your jacket."
        state.logbook_written = True
        return (
            "You uncap your pen and write: 'All quiet. On patrol.'\n\n"
            "You stare at it. It feels like a lie you haven't earned yet."
        )
    return "Write what, where?"


def handle_call(noun, player, state):
    if not noun:
        return "Call who?"
    noun = noun.lower()

    if not player.current_room.find_item("telephone") and \
       not player.has_item("radio") and \
       "maya" not in noun and "103" not in noun:
        return "You'd need a phone or radio for that."

    if "karen" in noun or "100" in noun or "supervisor" in noun:
        # Cooldown — Karen doesn't want to hear from you that often
        moves_since_karen = state.moves - state.last_karen_call
        if moves_since_karen < 20 and state.karen_calls > 0:
            return (
                "You reach for the radio.\n\n"
                "Static. A long hiss, like the building exhaling.\n\n"
                "Karen does not want to hear from you right now. "
                "This you understand instinctively."
            )
        state.last_karen_call = state.moves
        state.karen_calls += 1
        idx = min(state.karen_calls - 1, len(KAREN_CALLS) - 1)
        return KAREN_CALLS[idx]

    if "maya" in noun or "103" in noun or "cafe" in noun or "gift" in noun:
        if state.maya_called:
            return (
                "You try the gift shop extension again. "
                "It rings and rings. No answer.\n\n"
                "Maya has gone home. Into the blizzard. "
                "You hope she got there alright."
            )
        state.maya_called = True
        state.maya_met = True
        return (
            "You dial the gift shop extension. It rings four times. "
            "You're about to hang up —\n\n"
            "\"Hello?\" Maya's voice. Slightly breathless. "
            "The sound of someone still finishing closing duties.\n\n"
            "You tell her it's Nick. From security. You met earlier. "
            "You realize as you say it that you sound like an idiot.\n\n"
            "She laughs. It's a good laugh. Unguarded. "
            "\"I know who you are, Nick.\"\n\n"
            "A pause that isn't uncomfortable. "
            "That's new. That hasn't happened in a while.\n\n"
            "\"You doing okay out there? It's really coming down.\"\n\n"
            "You tell her you're fine. You tell her the coffee's terrible. "
            "She tells you she left the good stuff in the back, "
            "behind the counter, just put your name on it.\n\n"
            "You thank her.\n\n"
            "You almost say something else. You don't.\n\n"
            "\"Stay warm, Nick.\"\n\n"
            "She hangs up. The office feels quieter than it did "
            "before you called. You hadn't thought that was possible."
        )

    if "maintenance" in noun or "102" in noun:
        return (
            "You dial maintenance. It rings eleven times. "
            "Nobody answers.\n\n"
            "Maintenance is aware of the situation. "
            "Maintenance has gone home."
        )

    return f"You're not sure how to reach '{noun}' from here."


def handle_open(noun, player, state):
    if not noun:
        return "Open what?"
    item = player.current_room.find_item(noun) or player.get_item(noun)
    if not item:
        return f"You don't see any {noun} here."
    if hasattr(item, 'on_open'):
        return item.on_open(state)
    return item.on_examine(state)


def handle_use(noun, player, state):
    if not noun:
        return "Use what?"
    item = player.get_item(noun) or player.current_room.find_item(noun)
    if not item:
        # Special: use radio
        if "radio" in noun:
            if not player.has_item("radio"):
                return "The radio is on its charger. You should pick it up first."
            return handle_call("karen", player, state)
        return f"You don't see any {noun} here."
    return item.on_use(state)


def handle_turn_on(noun, player, state):
    if not noun:
        return "Turn on what?"
    if "flashlight" in noun or "light" in noun or "torch" in noun:
        state.flashlight_on = True
        return (
            "You click on the flashlight. "
            "A solid beam cuts the air in front of you. "
            "The battery indicator glows green. Good.\n\n"
            "It feels reassuring in a way you can't entirely justify."
        )
    if "radio" in noun:
        if not player.has_item("radio"):
            return "You'd need to pick up the radio first."
        state.radio_on = True
        return (
            "You power on the radio. "
            "It crackles with low static. "
            "Karen's channel hisses quietly. "
            "Somewhere in the building, the frequencies sound almost like breathing."
        )
    return f"You can't turn on the {noun}."


def handle_turn_off(noun, player, state):
    if "flashlight" in (noun or ""):
        state.flashlight_on = False
        return "You click off the flashlight. The darkness adjusts immediately."
    if "radio" in (noun or ""):
        state.radio_on = False
        return "You power down the radio. The static cuts out. The silence is worse."
    return f"You can't turn off the {noun}."


WAIT_MESSAGES = [
    "You stand still. The museum breathes around you.",
    "Time passes. The monitors hum. Monitor 7 shows static.",
    "You wait. Somewhere in the building, something clicks. Probably the heating.",
    "You are very good at standing in fluorescent light doing nothing. This is a skill.",
    "The blizzard presses against the windows. You wait.",
    "Danny is somewhere in this building, presumably also waiting. Less intentionally.",
    "You check your watch. Time is passing at its normal rate. This is reassuring.",
    "The whale skeleton hangs in the lobby, patient as it has been for forty years.",
    "You wait. The static on Monitor 7 doesn't change. You weren't expecting it to.",
    "Something in the sub-basement makes a sound. You wait anyway.",
]

WAIT_DREAD_MESSAGES = [
    # Fires after 50 waits — things getting weird
    "The lights flicker. Once. They come back.",
    "You hear something that might be footsteps from the floor above. There is no floor above you.",
    "Monitor 7's static shifts — almost a shape, almost recognizable. Then nothing.",
    "The temperature drops slightly. The HVAC cuts out. The silence is immediate and total.",
    "Something is watching the cameras. You feel this without being able to explain it.",
]

WAIT_DEATH = """
You have been standing here for a very long time.

The museum has noticed.

Something that has been patient — geological, oceanic, old in ways
that make the building's century feel like an afternoon — has been
watching you stand still. Waiting. As you have been waiting.

It decides you are not going to move on your own.

The lights go out. All of them. Simultaneously.
Monitor 7 resolves into perfect clarity for the first time.

You see what's been in the static.

You don't scream. There isn't time.

There isn't anything, after that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                     YOU HAVE DIED

            Cause of death: patience.
            The museum thanks you for your stillness.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


def handle_wait(player, state):
    state.wait_count = getattr(state, 'wait_count', 0) + 1

    if state.wait_count >= 200:
        print(WAIT_DEATH)
        sys.exit(0)

    if state.wait_count >= 50:
        # Escalating dread messages
        idx = min((state.wait_count - 50) // 10, len(WAIT_DREAD_MESSAGES) - 1)
        return WAIT_DREAD_MESSAGES[idx]

    return WAIT_MESSAGES[state.wait_count % len(WAIT_MESSAGES)]
    if "radio" in (noun or "") or not noun:
        if not player.has_item("radio"):
            return (
                "You can hear the low hum of the monitors. "
                "The distant groan of the building settling in the cold. "
                "The blizzard, pressing at the windows."
            )
        if state.radio_on:
            return (
                "Karen's channel is open. Static, mostly. "
                "Occasionally a distant burst of noise that might be "
                "interference from the storm.\n\n"
                "Might be."
            )
        return "The radio is off. You'd need to turn it on."
    return (
        "You listen. The museum breathes around you. "
        "Old buildings do this — the climate control, "
        "the settling of old stone. "
        "You tell yourself that's all it is."
    )


def handle_talk(noun, player, state):
    from rooms.main_lobby import maya
    if not noun:
        return "Talk to who?"
    noun_l = noun.lower()
    if "maya" in noun_l:
        if not maya.present:
            return (
                "Maya isn't here. She's gone home into the blizzard.\n\n"
                "You hope she made it okay."
            )
        result = maya.on_talk(state)
        maya.leave(how="talked")
        return result
    if "danny" in noun_l:
        return (
            "Danny isn't here right now. "
            "Danny is somewhere in the museum, being Danny.\n\n"
            "\"Sup,\" he would say, if he were here. "
            "That would be the end of the conversation."
        )
    if "karen" in noun_l:
        return handle_call("karen", player, state)
    return f"There's nobody called '{noun}' to talk to right now."


def handle_kiss(noun, player, state):
    from rooms.main_lobby import maya
    if "maya" in (noun or "").lower():
        if not maya.present:
            return "Maya isn't here. This is, in retrospect, fortunate."
        return maya.on_kiss(state)
    return "That's not something you can do right now."


def handle_hug(noun, player, state):
    from rooms.main_lobby import maya
    if "maya" in (noun or "").lower():
        if not maya.present:
            return "Maya's already gone."
        result = maya.on_hug(state)
        maya.leave(how="hugged")
        return result
    return "That's not something you can do right now."


def handle_ask(noun, player, state):
    from rooms.main_lobby import maya
    noun_l = (noun or "").lower()
    if "coffee" in noun_l or "chai" in noun_l or "drink" in noun_l:
        if not maya.present:
            return (
                "Maya's gone. "
                "She did leave you something behind the café counter, though."
            )
        result = maya.on_coffee(state)
        state.eat(35)
        maya.leave(how="coffee")
        return result
    if "maya" in noun_l:
        return handle_talk("maya", player, state)
    return "Ask who about what?"


def handle_sit(noun, player, state):
    noun_l = (noun or "").lower()
    if "bench" in noun_l or not noun:
        bench_item = player.current_room.find_item("bench")
        if bench_item:
            return (
                "You sit down.\n\n"
                "The bench is cold and hard and specifically uncomfortable "
                "in the way that public benches are uncomfortable on purpose, "
                "to discourage exactly this.\n\n"
                "You think about Danny, somewhere in the museum, "
                "having found himself a warm corner and committed to it "
                "with his entire being.\n\n"
                "You stand up.\n\n"
                "You're not Danny. You refuse to be Danny. "
                "This is the hill you've chosen."
            )
    return "There's nowhere particularly inviting to sit."


def handle_open_donations(player, state):
    from rooms.main_lobby import strange_coin, flattened_penny
    if getattr(state, 'donations_opened', False):
        return "You've already gone through the donation box. Once was enough."
    state.donations_opened = True
    strange_coin.taken = False
    flattened_penny.taken = False
    return (
        "The padlock opens on the third key you try.\n\n"
        "Inside:\n"
        "   A handful of change. Two Canadian quarters, which you resent.\n"
        "   A child's crayon drawing of the whale skeleton, "
        "labeled 'THE BIG FISH' with a smile drawn on it.\n"
        "   A folded note: 'For Timmy's school trip — thank you!! :)'\n"
        "   A flattened penny from the machine near the gift shop.\n\n"
        "And at the bottom — a coin you don't recognize. "
        "Cold to the touch.\n\n"
        "You pick it up.\n\n"
        "You feel like a person who opens donation boxes at midnight.\n"
        "Which is exactly what you are right now."
    )


def handle_flip_coin(player, state):
    if not player.has_item("strange coin") and not player.has_item("coin"):
        return "You'd need to be holding a coin for that."
    return (
        "It spins. You watch it spin.\n\n"
        "It lands. You look.\n\n"
        "Same face. Same mask.\n\n"
        "You put it in your pocket and don't flip it again."
    )


def handle_drop_coin(player, state):
    from rooms.main_lobby import strange_coin
    if not player.has_item("strange coin") and not player.has_item("coin"):
        return None
    return (
        "You set it on the floor and walk to the other side of the room.\n\n"
        "You check your pocket.\n\n"
        "It's there.\n\n"
        "You didn't pick it up.\n"
        "You're certain you didn't pick it up.\n\n"
        "You keep walking."
    )


def handle_help():
    return (
        "COLD SHIFT — Commands\n\n"
        "Movement:    NORTH / SOUTH / EAST / WEST (or N/S/E/W)\n"
        "Look:        LOOK (or L)\n"
        "Examine:     EXAMINE [object] (or X [object])\n"
        "Take:        TAKE [object] / GET [object]\n"
        "Drop:        DROP [object]\n"
        "Inventory:   INVENTORY (or I)\n"
        "Eat/Drink:   EAT [item] / DRINK [item]\n"
        "Read:        READ [item]\n"
        "Write:       WRITE [item]\n"
        "Use:         USE [item]\n"
        "Call:        CALL [person/number]\n"
        "Listen:      LISTEN\n"
        "Reverse:     REVERSE [item] — for when something seems backwards\n"
        "Turn on/off: TURN ON [item] / TURN OFF [item]\n\n"
        "Tips: Try examining everything. Try unusual verbs. "
        "Nick has opinions about most things."
    )


# ---------------------------------------------------------------------------
# MAIN DISPATCH
# ---------------------------------------------------------------------------

def dispatch(verb, noun, player, state):
    """Route parsed (verb, noun) to the right handler."""

    if verb == "go":
        return handle_go(noun, player, state)
    elif verb == "look":
        return handle_look(noun, player, state)
    elif verb == "take":
        return handle_take(noun, player, state)
    elif verb == "drop":
        return handle_drop(noun, player, state)
    elif verb == "inventory":
        return handle_inventory(player)
    elif verb == "eat":
        return handle_eat(noun, player, state)
    elif verb == "drink":
        return handle_drink(noun, player, state)
    elif verb == "read":
        return handle_read(noun, player, state)
    elif verb == "write":
        return handle_write(noun, player, state)
    elif verb == "call":
        return handle_call(noun, player, state)
    elif verb == "open":
        return handle_open(noun, player, state)
    elif verb == "use":
        return handle_use(noun, player, state)
    elif verb == "turn_on":
        return handle_turn_on(noun, player, state)
    elif verb == "turn_off":
        return handle_turn_off(noun, player, state)
    elif verb == "talk":
        return handle_talk(noun, player, state)
    elif verb == "kiss":
        return handle_kiss(noun, player, state)
    elif verb == "hug":
        return handle_hug(noun, player, state)
    elif verb == "ask":
        return handle_ask(noun, player, state)
    elif verb == "sit":
        return handle_sit(noun, player, state)
    elif verb == "flip":
        return handle_flip_coin(player, state)
    elif verb == "open":
        # Special case: donations box
        if noun and ("donat" in noun.lower() or "box" in noun.lower()):
            return handle_open_donations(player, state)
        return handle_open(noun, player, state)
    elif verb == "examine":
        # Special case: donations box examine also opens it
        if noun and ("donat" in noun.lower() or "donation box" in noun.lower()):
            return handle_open_donations(player, state)
        return handle_examine(noun, player, state)
    elif verb == "drop":
        # Special case: strange coin comes back
        if noun and "coin" in noun.lower():
            msg = handle_drop_coin(player, state)
            if msg:
                return msg
        return handle_drop(noun, player, state)
    elif verb == "wait":
        return handle_wait(player, state)
    elif verb == "listen":
        return handle_listen(noun, player, state)
    elif verb == "reverse":
        return handle_reverse(noun, player, state)
    elif verb == "help":
        return handle_help()
    elif verb == "quit":
        print("\nYou zip up your jacket and walk out into the blizzard.")
        print("Some nights you don't finish. This is one of them.")
        print("\n[ COLD SHIFT — abandoned ]")
        sys.exit(0)
    elif verb == "again":
        return None   # signal to repeat last command
    else:
        return (
            f"You're not sure how to '{verb}' that. "
            "Try HELP for a list of commands."
        )


# ---------------------------------------------------------------------------
# OPENING SEQUENCE
# ---------------------------------------------------------------------------

OPENING = """
╔══════════════════════════════════════════════════════════════╗
║                        COLD SHIFT                            ║
║                   A Game of Creeping Dread                   ║
║                                                              ║
║    Miskatonic Museum of Natural History and Antiquities      ║
║                  December 19th. 11:02 PM.                    ║
╚══════════════════════════════════════════════════════════════╝

Outside, the blizzard that the weather service spent three days
threatening has finally arrived and is making up for lost time.
Inside, six floors of dead things, old bones, and priceless
artifacts are yours until 6 AM.

First week on the job.

You've had worse weeks. You're trying to remember when.

Your radio crackles before you've even hung up your jacket.

"Callahan." Karen. Already. "We have a crate in the Hall of
Ancient Civilizations. Acquisitions left it there — don't ask.
It stays roped off. You don't touch it. You don't let anyone
touch it. Clear?"

You tell her it's clear.

"And Callahan — Danny knows the rounds. Follow his lead."

She clicks off. Somewhere in the museum, presumably, Danny is
following his lead directly into a warm corner and a long nap.

You pour yourself a cup of coffee.

First week on the job.

──────────────────────────────────────────────────────────────
"""


# ---------------------------------------------------------------------------
# GAME LOOP
# ---------------------------------------------------------------------------

def main():
    print(OPENING)

    state = GameState()
    player = Player()

    starting_room, main_lobby = build_world()
    player.current_room = starting_room

    # First room description
    print(starting_room.describe(state))
    print()

    last_verb = None
    last_noun = None

    while not state.game_over:
        # Maya timeout check
        if hasattr(main_lobby, 'check_maya_timeout'):
            maya_msg = main_lobby.check_maya_timeout(state.moves)
            if maya_msg:
                print(f"\n{maya_msg}\n")

        # Pepper spray effect
        from rooms.main_lobby import maya
        if maya.pepper_spray_turns > 0:
            maya.pepper_spray_turns -= 1
            if maya.pepper_spray_turns > 0:
                print(
                    f"\n(Your eyes are still burning. "
                    f"{maya.pepper_spray_turns} turns of consequences remaining.)\n"
                )

        # Hunger check
        hunger_msg = state.get_hunger_message()
        if hunger_msg:
            print(f"\n{hunger_msg}\n")

        # Karen check
        karen_interrupts(state)

        # Ambient message (random)
        ambient = player.current_room.get_ambient()
        if ambient:
            print(f"\n{ambient}\n")

        # Prompt
        try:
            raw = input("> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n[ COLD SHIFT — session ended ]")
            sys.exit(0)

        if not raw:
            continue

        # Parse
        verb, noun = parse(raw)

        # Handle AGAIN
        if verb == "again":
            if last_verb:
                verb, noun = last_verb, last_noun
            else:
                print("(Nothing to repeat.)")
                continue

        if verb is None:
            responses = [
                "That's not something you know how to do.",
                "The museum offers no guidance on that.",
                "Nick stares at the middle distance. That didn't work.",
                "You'll need to try something else.",
            ]
            print(random.choice(responses))
            continue

        # Dispatch
        result = dispatch(verb, noun, player, state)
        if result:
            print(f"\n{result}\n")

        # Store for AGAIN
        last_verb = verb
        last_noun = noun

        # Tick state
        state.tick()


if __name__ == "__main__":
    main()
