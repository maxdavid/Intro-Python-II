from style import color


class Item:
    def __init__(self, name, description="", weight=0, actions=[]):
        self.name = name
        self.description = description
        self.weight = weight
        self.actions = actions

    def __repr__(self):
        return f"Item({self.name})"

    def __str__(self):
        return f"{color.BOLD}{color.GREEN}{self.name}{color.END} : {self.description}"

