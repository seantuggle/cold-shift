# rooms/security_office.py
# The Security Office. Nick's home base.
# First room. Establishes everything.

from room import Room
from items import Item, ConsumableItem, ContainerItem


# ---------------------------------------------------------------------------
# ITEMS
# ---------------------------------------------------------------------------

# --- Starting inventory items (described but not room items) ---
# These are handled in player.py as fixed starting inventory.
# Nick always has: cell phone, gum, keys, wallet, flashlight.

# --- Consumables ---

ramen = ConsumableItem(
    name="ramen",
    aliases=["noodles", "container", "ramen noodles", "cold ramen", "food"],
    description=(
        "A plastic container of cold ramen noodles, Danny's name written "
        "on the lid in marker. The noodles have congealed in that specific "
        "way that suggests they've been in there since Tuesday. "
        "A plastic fork is wedged under the lid.\n\n"
        "Not yours. You're going to eat it anyway. This feels like growth."
    ),
    eat_text=(
        "You eat the ramen standing up, looking at Monitor 7.\n\n"
        "It's not good. It's not bad. It's fuel, and you're a machine "
        "that needs to get to 6 AM. You've eaten sadder things in "
        "sadder kitchens.\n\n"
        "You think about the last meal you cooked for Avery. Pancakes. "
        "She said they tasted like cardboard. You told her that was "
        "the secret ingredient.\n\n"
        "You put the empty container in the trash and feel nothing "
        "and everything simultaneously."
    ),
    hunger_reset=40,
    takeable=True,
)

soda = ConsumableItem(
    name="soda",
    aliases=["can", "soda can", "pop"],
    description=(
        "A generic-brand energy soda, the kind that comes in a can "
        "the color of a warning sign. It's been in the fridge long enough "
        "to be properly cold. Nobody has claimed it. It's yours now."
    ),
    eat_text=(
        "You crack it open. It hisses like it's been waiting months "
        "for this moment.\n\n"
        "Cold, sweet, aggressively caffeinated. Exactly what you needed. "
        "Small mercies.\n\n"
        "(You feel slightly more alert. This will not save you.)"
    ),
    hunger_reset=20,
    takeable=True,
)

sports_drink = ConsumableItem(
    name="sports drink",
    aliases=["bottle", "gatorade", "drink", "sports bottle"],
    description=(
        "A plastic bottle, roughly half full, the cap replaced with "
        "the optimism of someone who genuinely intended to finish it. "
        "Danny's, almost certainly. The liquid is an aggressive shade "
        "of purple that doesn't occur in nature."
    ),
    eat_text=(
        "You pick up the bottle. Half full. Someone else's backwash. "
        "Danny's, in all likelihood.\n\n"
        "You think about it.\n\n"
        "You drink it anyway. It tastes like artificial grape "
        "and compromise.\n\n"
        "(Hydrated. For what it's worth.)"
    ),
    hunger_reset=15,
    takeable=True,
)

coffee = ConsumableItem(
    name="coffee",
    aliases=["cup", "styrofoam", "styrofoam cup", "coffee cup"],
    description=(
        "A styrofoam cup, half full. You made this coffee an hour ago "
        "and it was bad then. It has since passed through several "
        "emotional stages. It is now in the acceptance phase."
    ),
    eat_text=(
        "You drink the coffee.\n\n"
        "It tastes like it was brewed from regret and a filter "
        "that's been used one time too many.\n\n"
        "You drink it anyway. It's warm. It's something to do "
        "with your hands. This is your life now.\n\n"
        "You've had worse lives. You're trying to remember when.\n\n"
        "(Coffee consumed. You are marginally more awake and "
        "significantly more aware of your life choices.)"
    ),
    hunger_reset=10,
    takeable=True,
)

hot_sauce = ConsumableItem(
    name="hot sauce",
    aliases=["hot sauce packets", "packets", "sauce", "hot sauce packet"],
    description=(
        "Three packets of hot sauce from a fast food place that "
        "stopped existing approximately two years ago. "
        "Danny's, obviously. They've been here a while."
    ),
    eat_text=(
        "You tear open a packet and squeeze it onto your tongue "
        "because that is apparently who you are now.\n\n"
        "It's not spicy so much as it is an aggressive memory "
        "of spice. Chemical heat. You regret this immediately "
        "and completely.\n\n"
        "(Negligible. But you feel something, which counts.)"
    ),
    hunger_reset=5,
    takeable=True,
)

# --- Mini fridge ---

fridge = ContainerItem(
    name="fridge",
    aliases=["mini fridge", "refrigerator", "minifridge"],
    description=(
        "A mini-fridge of uncertain vintage squatting in the corner "
        "like it's waiting for an apology. It hums with the specific "
        "frequency of something that has never been cleaned."
    ),
    contents=[ramen, soda, sports_drink],
)

# --- Functional items ---

logbook = Item(
    name="logbook",
    aliases=["log", "log book", "book", "patrol log"],
    description=(
        "The official security logbook, thick with years of uneventful "
        "nights. You flip back through Danny's recent entries:\n\n"
        "   'All good.'\n"
        "   'All good.'\n"
        "   'All good.'\n"
        "   'Quiet night. Vending machine ate my dollar again. "
        "Filing a formal complaint with no one.'\n"
        "   'All good.'\n"
        "   'weird smell in sub basement dont worry about it'\n"
        "   'All good.'\n"
        "   'Crate showed up. Karen says dont touch it. "
        "Not touching it. It makes a sound sometimes. "
        "Not writing that down officially.'\n\n"
        "Your entry line is blank."
    ),
    takeable=False,
)

telephone = Item(
    name="telephone",
    aliases=["phone", "landline", "desk phone", "land line"],
    description=(
        "Institutional grey, the color of bureaucratic resignation. "
        "A piece of masking tape on the handset:\n\n"
        "   EXT. 100 — SUPERVISOR\n"
        "   EXT. 102 — MAINTENANCE\n"
        "   EXT. 103 — GIFT SHOP/CAFE\n\n"
        "Below, in Danny's handwriting: 'dont call 100 unless dying. "
        "maybe not even then'"
    ),
    takeable=False,
)

radio = Item(
    name="radio",
    aliases=["walkie talkie", "walkie-talkie", "two way radio", "two-way"],
    description=(
        "A standard-issue security radio, currently sitting on its "
        "charging dock on the shelf. The charging light glows green. "
        "A strip of tape on the back reads CALLHAN in Karen's handwriting.\n\n"
        "Even your radio has your name wrong."
    ),
    takeable=True,
)

schedule = Item(
    name="schedule",
    aliases=["patrol schedule", "patrol route", "karen's schedule",
             "karens schedule", "rota"],
    description=(
        "Karen's patrol schedule, marked in thirty-minute increments "
        "with the totalitarian precision of someone who has never once "
        "had an interesting night.\n\n"
        "Your name — CALLHAN — is circled at the top. Below:\n\n"
        "   'DO NOT TOUCH THE CRATE.\n"
        "   DO NOT ENTER RESTRICTED AREAS.\n"
        "   IF IN DOUBT, CALL EXT. 100.\n"
        "   — K'\n\n"
        "Below that, in the smallest possible handwriting:\n"
        "   'P.S. Sub-basement camera out 3 weeks. Maint. aware.'\n\n"
        "Maintenance is aware. Great."
    ),
    takeable=False,
)

postit = Item(
    name="post-it",
    aliases=["post it", "sticky note", "yellow note", "note", "postit"],
    description=(
        "A yellow Post-it note — appropriately enough — stuck to the "
        "corkboard at an angle, like it was added in a hurry. "
        "The handwriting is cramped and slightly uneven:\n\n"
        "   rears untruths\n\n"
        "Below it, a date. Three years ago. Nothing else.\n\n"
        "You stare at it. It looks like a password someone would make up "
        "after a head injury. Some instinct makes you take it down "
        "and pocket it anyway."
    ),
    takeable=True,
)

corkboard = Item(
    name="corkboard",
    aliases=["board", "cork board", "bulletin board", "wall"],
    description=(
        "Karen's patrol schedule. A fire evacuation map. A memo about "
        "acceptable footwear on museum floors — you're fine. "
        "The Christmas party notice: December 23rd, bring a dish to share, "
        "RSVP to Karen. Someone has drawn a small frowning face on it "
        "in blue pen.\n\n"
        "Definitely Danny.\n\n"
        "And a yellow Post-it note with something written on it."
    ),
    takeable=False,
)

monitors = Item(
    name="monitors",
    aliases=["monitor", "screens", "cameras", "feeds", "security monitors",
             "cctv", "camera feeds"],
    description=(
        "Sixteen feeds. You've memorized them already because that is, "
        "apparently, your life now.\n\n"
        "Loading dock: empty. Gift shop: dark. Rotunda: the whale skeleton "
        "hangs in the black like it's judging you. East corridor: empty. "
        "West corridor: empty. Natural History Wing: empty.\n\n"
        "Hall of Ancient Civilizations: static. Monitor 7. "
        "You tap the screen. The static remains committed to its position.\n\n"
        "You made a note. The note joins other notes on the desk. "
        "This feels like progress and isn't."
    ),
    takeable=False,
)

monitor_7 = Item(
    name="monitor 7",
    aliases=["monitor seven", "monitor7", "static", "channel 7"],
    description=(
        "You lean in close. The static is just static. "
        "Interference from the blizzard, probably. Old equipment. "
        "These things happen.\n\n"
        "There is a shape in it.\n\n"
        "There isn't.\n\n"
        "You sit back down."
    ),
    takeable=False,
)

# --- Danny's area ---

dannys_desk = Item(
    name="danny's desk",
    aliases=["desk", "other desk", "messy desk", "dannys desk"],
    description=(
        "Danny's desk looks like the aftermath of a negotiation between "
        "several fast food bags and a man who stopped caring who won. "
        "A constellation of hot sauce packets. Three pens, none of them "
        "with caps. A motivational calendar, still open to October. "
        "A crumpled wrestling magazine. Something that might be a sock.\n\n"
        "Under the wrestling magazine: a crumpled note."
    ),
    takeable=False,
)

dannys_note = Item(
    name="danny's note",
    aliases=["crumpled note", "note under magazine", "note"],
    description=(
        "You smooth it out. Danny's handwriting — large, looping, "
        "the handwriting of a man at peace with taking up space:\n\n"
        "   'weird smell in sub basement. like the ocean but wrong. "
        "also the lights flicker down there. told karen. karen said "
        "thats just the building. buildings dont smell like the ocean karen'\n\n"
        "You put the note in your pocket. Against your better judgment, "
        "you find Danny more interesting than you did five minutes ago."
    ),
    takeable=True,
)

magazine = Item(
    name="magazine",
    aliases=["wrestling magazine", "wresting mag", "mag"],
    description=(
        "A wrestling magazine, six months old, creased down the spine "
        "from being read cover to cover at least twice. "
        "The cover features two men in the process of doing something "
        "that looks painful and theatrical simultaneously.\n\n"
        "Danny has circled several wrestlers' names. "
        "Next to one he's written 'me someday' in ballpoint pen.\n\n"
        "You put it back. Some things you don't need to know about a person."
    ),
    takeable=False,
)

calendar = Item(
    name="calendar",
    aliases=["motivational calendar", "wall calendar", "desk calendar"],
    description=(
        "A motivational calendar, still open to October. "
        "October's message: 'YOU ARE CAPABLE OF MORE THAN YOU KNOW.'\n\n"
        "It's December 19th.\n\n"
        "Danny has been getting this motivational message every day "
        "for two months. You consider what this says about Danny. "
        "You consider what it says about the calendar. "
        "You consider what it says about the concept of motivation.\n\n"
        "You close the calendar to October and walk away."
    ),
    takeable=False,
)

sock = Item(
    name="sock",
    aliases=["mystery sock", "the sock"],
    description=(
        "You look at the sock.\n\n"
        "The sock looks back.\n\n"
        "No. You're not doing this. You have standards. "
        "Diminished, yes. Situational, certainly. "
        "But they exist and they include not investigating "
        "unidentified socks found under a coworker's desk.\n\n"
        "You walk away."
    ),
    takeable=False,
)

# --- Purely flavor items (do nothing, just have character) ---

stapler = Item(
    name="stapler",
    aliases=[],
    description=(
        "A standard office stapler, red, sitting on a shelf. "
        "You try it. It clicks emptily. "
        "Out of staples. Has probably been out of staples for months. "
        "Nobody has refilled it. Nobody will.\n\n"
        "You and this stapler have a lot in common right now."
    ),
    takeable=False,
)

plant = Item(
    name="plant",
    aliases=["dead plant", "dying plant", "fern", "potted plant"],
    description=(
        "A small potted plant on the shelf near the fridge, "
        "doing its level best to stay alive on nothing but "
        "fluorescent light and ambient despair.\n\n"
        "About half the leaves are brown. The soil is bone dry. "
        "Somebody put it here and then forgot about it.\n\n"
        "You water it from the sports drink bottle if you have it. "
        "Or you don't. Either way, the plant's prospects are grim.\n\n"
        "You relate to this plant."
    ),
    takeable=False,
)

novelty_mug = Item(
    name="mug",
    aliases=["novelty mug", "coffee mug", "ceramic mug"],
    description=(
        "A ceramic mug on the shelf that reads: "
        "'WORLD'S OKAYEST SECURITY GUARD'.\n\n"
        "Below that, in smaller text: 'Don't Touch Danny's Mug'.\n\n"
        "You didn't touch Danny's mug."
    ),
    takeable=False,
)

lost_and_found = Item(
    name="lost and found",
    aliases=["lost and found box", "lost & found", "box"],
    description=(
        "A cardboard box near the door labeled LOST & FOUND "
        "in permanent marker. You look inside.\n\n"
        "Contents: one child's mitten (left hand), a paperback novel "
        "with the last forty pages torn out, a set of keys to a "
        "car that no longer exists in this parking lot, "
        "and a small ceramic owl that stares at you with "
        "an unsettling degree of personality.\n\n"
        "You leave everything where it is. "
        "Some things are lost for good reasons."
    ),
    takeable=False,
)

mirror = Item(
    name="mirror",
    aliases=["small mirror", "wall mirror"],
    description=(
        "A small mirror screwed to the wall by the door — "
        "the kind put there so you can check your uniform "
        "before starting a shift.\n\n"
        "You look at yourself.\n\n"
        "You look like a man who has been awake longer than he should be, "
        "doing a job he didn't plan on having, "
        "in a December that has not been kind.\n\n"
        "Your badge still says NICK, at least. "
        "They got that one right."
    ),
    takeable=False,
)

# --- Nick's own desk items ---

nicks_desk = Item(
    name="my desk",
    aliases=["my desk", "nicks desk", "nick's desk", "clean desk",
             "your desk"],
    description=(
        "Your desk. Clean. Aggressively, defiantly clean. "
        "You cleaned it on your first night with the quiet fury "
        "of a man who can't control much right now but can control this.\n\n"
        "On it: the logbook, the telephone, a cup of coffee "
        "that has passed through several emotional stages."
    ),
    takeable=False,
)


# ---------------------------------------------------------------------------
# ROOM FACTORY
# ---------------------------------------------------------------------------

def make_security_office():
    """Build and return the fully populated Security Office room."""

    long_desc = (
        "SECURITY OFFICE\n\n"
        "A room that gave up on itself years ago and has been coasting "
        "ever since. The carpet is the color of a decision nobody remembers "
        "making. Sixteen monitors line the north wall, showing grainy "
        "black-and-white feeds of a museum that contains, by all appearances, "
        "nothing but darkness and the occasional startled shadow.\n\n"
        "Fifteen feeds show empty corridors and hushed exhibit halls. "
        "Monitor 7 shows static. It has been showing static since you "
        "arrived. You are not thinking about Monitor 7.\n\n"
        "Your desk is clean — mercilessly, defiantly clean, because you "
        "needed one thing in your life right now that you could control. "
        "Danny's desk is something else entirely. His chair sits empty "
        "in a landscape of fast food archaeology and misplaced optimism.\n\n"
        "A battered mini-fridge squats in the corner. "
        "Above your desk, a corkboard holds Karen's patrol schedule "
        "and other items of varying importance. "
        "The radio sits on its charging dock on the shelf, green light on.\n\n"
        "A door leads north to the Main Lobby."
    )

    short_desc = (
        "SECURITY OFFICE\n\n"
        "Yours is still clean. Danny's still isn't. "
        "The monitors hum. Monitor 7 still shows static. "
        "The coffee, at this point, is archaeological."
    )

    ambient = [
        "The monitors hum their low, indifferent hum.",
        (
            "Somewhere in the museum, a climate control vent "
            "shudders and goes quiet."
        ),
        (
            "You think about Avery. You think about the drive home after. "
            "You think about the empty apartment waiting for you at 6 AM. "
            "You think about something else instead."
        ),
        (
            "The static on Monitor 7 seems, for just a moment, to resolve "
            "into a shape. Then it doesn't."
        ),
        (
            "The blizzard presses against the building like it's trying "
            "to get in. The building holds. So far."
        ),
        (
            "Danny's chair sits empty. You wonder where he goes. "
            "You decide he's a grown man capable of finding his own "
            "warm corner, which, honestly, sounds pretty good right now."
        ),
        (
            "The Christmas party notice catches your eye. "
            "December 23rd. You were supposed to spend Christmas "
            "somewhere else this year. With someone else.\n"
            "You look at something else."
        ),
    ]

    room = Room(
        name="Security Office",
        short_desc=short_desc,
        long_desc=long_desc,
        exits={"north": None},   # north -> Main Lobby, wired in world.py
    )

    room.ambient_messages = ambient

    # All items present in the room
    room.items = [
        monitors, monitor_7, logbook, telephone, radio,
        schedule, corkboard, postit,
        coffee, fridge,          # fridge contains ramen, soda, sports_drink
        ramen, soda, sports_drink, hot_sauce,
        nicks_desk, dannys_desk, dannys_note,
        magazine, calendar, sock,
        stapler, plant, novelty_mug, lost_and_found, mirror,
    ]

    return room
