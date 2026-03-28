# parser.py
# Turns raw player input into structured (verb, noun) pairs.
# Infocom-style: handles common synonyms and multi-word inputs.

# Verb synonym map — all synonyms collapse to a canonical verb
VERB_MAP = {
    # movement
    "go": "go", "move": "go", "walk": "go", "head": "go",
    "north": "go", "south": "go", "east": "go", "west": "go",
    "up": "go", "down": "go", "n": "go", "s": "go",
    "e": "go", "w": "go", "u": "go", "d": "go",

    # look / examine
    "look": "look", "l": "look",
    "examine": "examine", "x": "examine", "ex": "examine",
    "inspect": "examine", "check": "examine", "describe": "examine",
    "read": "read",
    "watch": "examine",

    # take / drop
    "take": "take", "get": "take", "grab": "take",
    "pick": "take", "carry": "take",
    "drop": "drop", "put": "drop", "leave": "drop",
    "set": "drop", "place": "drop",

    # inventory
    "inventory": "inventory", "i": "inventory", "inv": "inventory",
    "pockets": "inventory",

    # use / interact
    "use": "use", "activate": "use", "operate": "use",
    "open": "open",
    "wear": "wear", "put on": "wear",
    "remove": "remove", "take off": "remove",
    "eat": "eat", "consume": "eat", "taste": "eat",
    "drink": "drink", "sip": "drink", "swallow": "drink",
    "call": "call", "phone": "call", "dial": "call",
    "radio": "call",
    "write": "write", "sign": "write", "fill": "write",
    "turn on": "turn_on", "switch on": "turn_on",
    "turn off": "turn_off", "switch off": "turn_off",
    "etch": "etch", "rub": "etch", "trace": "etch",
    "reverse": "reverse", "flip": "reverse",
    "speak": "speak", "say": "speak", "recite": "speak",
    "listen": "listen",

    "shake": "shake", "grab": "shake",
    "slap": "slap", "hit": "slap", "smack": "slap",

    # social
    "talk": "talk", "speak to": "talk", "talk to": "talk",
    "greet": "talk", "chat": "talk",
    "kiss": "kiss",
    "hug": "hug", "embrace": "hug",
    "ask": "ask",
    "sit": "sit", "sit on": "sit", "sit down": "sit",
    "flip": "flip",

    # wait
    "wait": "wait", "z": "wait",

    # meta
    "help": "help", "?": "help",
    "quit": "quit", "exit": "quit", "q": "quit",
    "save": "save", "load": "load",
    "again": "again", "g": "again",
}

# Direction aliases for GO
DIRECTIONS = {
    "north": "north", "n": "north",
    "south": "south", "s": "south",
    "east": "east", "e": "east",
    "west": "west", "w": "west",
    "up": "up", "u": "up",
    "down": "down", "d": "down",
}

# Words to strip from input before parsing
STOP_WORDS = {
    "the", "a", "an", "at", "to", "on", "in", "into",
    "with", "of", "up", "it", "that", "this",
}


def parse(raw_input):
    """
    Parse raw player input into (verb, noun_string).
    Returns (verb, noun) tuple. noun may be None.
    verb will be None if input is unrecognized.
    """
    raw = raw_input.lower().strip()
    if not raw:
        return (None, None)

    # Handle multi-word verb phrases before splitting
    for phrase in ["turn on", "turn off", "switch on", "switch off",
                   "pick up", "put on", "take off"]:
        if raw.startswith(phrase):
            canonical = VERB_MAP.get(phrase, phrase.replace(" ", "_"))
            noun = raw[len(phrase):].strip()
            noun = _clean_noun(noun)
            return (canonical, noun or None)

    tokens = raw.split()

    # Single token — could be direction or verb
    if len(tokens) == 1:
        token = tokens[0]
        if token in DIRECTIONS:
            return ("go", token)
        verb = VERB_MAP.get(token)
        if verb:
            return (verb, None)
        return (None, None)

    # First token is verb, rest is noun phrase
    verb_raw = tokens[0]

    # Special: "go north" vs just "north"
    if verb_raw == "go" and len(tokens) > 1:
        direction = DIRECTIONS.get(tokens[1])
        if direction:
            return ("go", direction)

    verb = VERB_MAP.get(verb_raw)
    if not verb:
        return (None, None)

    # Clean up noun phrase
    noun_tokens = [t for t in tokens[1:] if t not in STOP_WORDS]
    noun = " ".join(noun_tokens) if noun_tokens else None
    return (verb, noun)


def _clean_noun(noun):
    """Strip stop words from a noun phrase."""
    tokens = [t for t in noun.split() if t not in STOP_WORDS]
    return " ".join(tokens) if tokens else None
