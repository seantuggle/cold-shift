# player.py
# Nick. His inventory, his condition, his voice.

class Player:
    def __init__(self):
        self.inventory = []
        self.current_room = None
        self.flashlight_on = False

    def take(self, item, state):
        """Move item from room to inventory."""
        result = item.on_take(state)
        if item.taken:
            if item in self.current_room.items:
                self.current_room.items.remove(item)
            self.inventory.append(item)
        return result

    def drop(self, item, state):
        """Move item from inventory to current room."""
        result = item.on_drop(state)
        if not item.taken:
            self.inventory.remove(item)
            self.current_room.items.append(item)
        return result

    def has_item(self, item_name):
        """Check inventory by name or alias."""
        for item in self.inventory:
            if item.matches(item_name):
                return True
        return False

    def get_item(self, item_name):
        """Get item from inventory by name or alias."""
        for item in self.inventory:
            if item.matches(item_name):
                return item
        return None

    def inventory_list(self):
        if not self.inventory:
            return (
                "Your pockets contain: a cell phone, a stick of gum, "
                "your keys, your wallet, and a flashlight.\n"
                "You are carrying nothing else.\n\n"
                "You are a man of few possessions right now. "
                "This is new."
            )
        items = [i.name for i in self.inventory]
        # Always show starting items flavor
        base = (
            "Your pockets: cell phone, gum, keys, wallet, flashlight."
        )
        carried = "You're also carrying: " + ", ".join(items) + "."
        return base + "\n" + carried
