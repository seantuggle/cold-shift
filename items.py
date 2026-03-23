# items.py
# Base Item class and all item interaction logic.
# Each item knows its own name, description, and what happens
# when the player tries various verbs on it.

class Item:
    def __init__(self, name, aliases, description, takeable=False, consumable=False):
        self.name = name
        self.aliases = aliases          # list of strings player might type
        self.description = description  # examine text
        self.takeable = takeable
        self.consumable = consumable
        self.taken = False              # True once in player inventory
        self.consumed = False           # True once eaten/drunk

    def matches(self, word):
        """Returns True if word matches this item's name or any alias."""
        word = word.lower().strip()
        return word == self.name.lower() or word in [a.lower() for a in self.aliases]

    def on_examine(self, state):
        """Default examine. Rooms/items can override for dynamic text."""
        return self.description

    def on_take(self, state):
        if not self.takeable:
            return "You can't take that."
        if self.taken:
            return "You're already carrying that."
        self.taken = True
        return f"You take the {self.name}."

    def on_drop(self, state):
        if not self.taken:
            return "You don't have that."
        self.taken = False
        return f"You set down the {self.name}."

    def on_use(self, state):
        return f"You're not sure how to use the {self.name} right now."

    def on_eat(self, state):
        if not self.consumable:
            return f"You can't eat the {self.name}. Even by your current standards."
        if self.consumed:
            return f"There's nothing left of the {self.name}."
        return None  # subclasses handle actual consumption

    def on_drink(self, state):
        return self.on_eat(state)

    def on_read(self, state):
        return f"There's nothing to read on the {self.name}."

    def on_wear(self, state):
        return f"You can't wear the {self.name}."


class ConsumableItem(Item):
    """An item that can be eaten or drunk, resetting hunger by some amount."""
    def __init__(self, name, aliases, description,
                 eat_text, hunger_reset, takeable=True):
        super().__init__(name, aliases, description,
                         takeable=takeable, consumable=True)
        self.eat_text = eat_text
        self.hunger_reset = hunger_reset   # moves added back to hunger clock

    def on_eat(self, state):
        base = super().on_eat(state)
        if base:
            return base
        self.consumed = True
        state.eat(self.hunger_reset)
        return self.eat_text

    def on_drink(self, state):
        return self.on_eat(state)


class ContainerItem(Item):
    """An item that holds other items (fridge, desk, jacket)."""
    def __init__(self, name, aliases, description, contents=None):
        super().__init__(name, aliases, description, takeable=False)
        self.contents = contents or []

    def on_examine(self, state):
        if not self.contents:
            return self.description + "\n\nIt's empty."
        content_names = ", ".join(
            f"a {i.name}" for i in self.contents if not i.consumed and not i.taken
        )
        if not content_names:
            return self.description + "\n\nIt's empty now."
        return self.description + f"\n\nInside: {content_names}."

    def on_open(self, state):
        return self.on_examine(state)
