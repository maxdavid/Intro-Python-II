class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def add_item(self, item):
        self.items.append(item)
        return self.items

    def drop_item(self, item):
        try:
            self.items.remove(item)
            return self.items
        except:
            return self.items

    def __repr__(self):
        return f"Player({self.name}) at {repr(self.current_room)}"

    def __str__(self):
        return f"{self.name}"

