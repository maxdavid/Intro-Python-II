from textwrap import wrap
from style import color


class Room:
    def __init__(self, name, description="", items=[]):
        self.name = name
        self.description = "\n".join(wrap(description, 80))
        self.items = items
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def add_item(self, item):
        self.items.append(item)
        return self.items

    def __repr__(self):
        return f"Room({self.name})"

    def __str__(self):
        return f"{color.BOLD}{self.name}{color.END} : {self.description}"

