# room.py
# Base Room class. Every room in Cold Shift inherits from this.

import random

class Room:
    def __init__(self, name, short_desc, long_desc, exits=None):
        self.name = name
        self.short_desc = short_desc    # shown on return visits
        self.long_desc = long_desc      # shown on first visit or LOOK
        self.exits = exits or {}        # dict: direction -> Room
        self.items = []                 # items currently in this room
        self.visited = False
        self.ambient_messages = []      # list of strings, fire randomly
        self.first_visit_event = None   # callable(state) -> str, fires once

    def describe(self, state):
        """Full room description. Uses long on first visit, short after."""
        if not self.visited:
            self.visited = True
            desc = self.long_desc
            if self.first_visit_event:
                event_text = self.first_visit_event(state)
                if event_text:
                    desc = event_text + "\n\n" + desc
        else:
            desc = self.short_desc

        # List visible items
        visible = [i for i in self.items if not i.taken and not i.consumed]
        if visible:
            item_line = "You can see: " + ", ".join(
                f"a {i.name}" for i in visible
            ) + "."
            desc += "\n\n" + item_line

        # Exits
        if self.exits:
            exit_line = "Exits: " + ", ".join(
                d.capitalize() for d in self.exits
            ) + "."
            desc += "\n\n" + exit_line

        return desc

    def look(self, state):
        """LOOK always returns long description."""
        desc = self.long_desc
        visible = [i for i in self.items if not i.taken and not i.consumed]
        if visible:
            item_line = "You can see: " + ", ".join(
                f"a {i.name}" for i in visible
            ) + "."
            desc += "\n\n" + item_line
        if self.exits:
            exit_line = "Exits: " + ", ".join(
                d.capitalize() for d in self.exits
            ) + "."
            desc += "\n\n" + exit_line
        return desc

    def get_ambient(self):
        """Returns a random ambient message or None."""
        if self.ambient_messages and random.random() < 0.3:
            return random.choice(self.ambient_messages)
        return None

    def find_item(self, word):
        """Find an item in this room by name or alias."""
        for item in self.items:
            if item.matches(word) and not item.taken:
                return item
        return None
