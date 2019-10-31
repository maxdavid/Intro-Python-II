from room import Room
from player import Player
from item import Item
from style import color

titlecard = """
 ██▓███ ▓██   ██▓   ▓█████▄  █    ██  ███▄    █   ▄████ ▓█████  ▒█████   ███▄    █ 
▓██░  ██▒▒██  ██▒   ▒██▀ ██▌ ██  ▓██▒ ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▒██▒  ██▒ ██ ▀█   █ 
▓██░ ██▓▒ ▒██ ██░   ░██   █▌▓██  ▒██░▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▒██░  ██▒▓██  ▀█ ██▒
▒██▄█▓▒ ▒ ░ ▐██▓░   ░▓█▄   ▌▓▓█  ░██░▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██   ██░▓██▒  ▐▌██▒
▒██▒ ░  ░ ░ ██▒▓░   ░▒████▓ ▒▒█████▓ ▒██░   ▓██░░▒▓███▀▒░▒████▒░ ████▓▒░▒██░   ▓██░
▒▓▒░ ░  ░  ██▒▒▒     ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
░▒ ░     ▓██ ░▒░     ░ ▒  ▒ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
░░       ▒ ▒ ░░      ░ ░  ░  ░░░ ░ ░    ░   ░ ░ ░ ░   ░    ░   ░ ░ ░ ▒     ░   ░ ░ 
         ░ ░           ░       ░              ░       ░    ░  ░    ░ ░           ░ 
         ░ ░         ░                                                             
"""

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        "Dim light filters in from the south. Dusty passages run north and east.",
    ),
    "overlook": Room(
        "Grand Overlook",
        "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.",
    ),
    "narrow": Room(
        "Narrow Passage",
        "The narrow passage bends here from west to north. The smell of gold permeates the air.",
    ),
    "treasure": Room(
        "Treasure Chamber",
        "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",
    ),
}

item = {
    "sword": Item(
        "Sword",
        "A sharp steel sword of journeyman quality.",
        5,
        {
            "swing": "You swing the sword through the air, hitting nothing in particular.",
            "sheath": "You sheath the sword into your leather scabbard.",
            "unsheath": "You quickly unsheath your sword!",
        },
    ),
    "lantern": Item(
        "Lantern",
        "A small oil lamp for illuminating the darkness.",
        1,
        {
            "light": "You light the lantern, illuminating the area around you.",
            "extinguish": "You extinguish the lantern, plunging the area around you into darkness.",
        },
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

# Add items to rooms
room["foyer"].add_item(item["lantern"])
room["overlook"].add_item(item["sword"])

#
# Main
#

avatar = """
      _,.
    ,` -.)
   ( _/-\\-._
  /,|`--._,-^|            ,
  \_| |`-._/||          ,'|
    |  `-, / |         /  /
    |     || |        /  /
     `r-._||/   __   /  /
 __,-<_     )`-/  `./  /
'  \   `---'   \   /  /
    |           |./  /
    /           //  /
\_/' \         |/  /
 |    |   _,^-'/  /
 |    , ``  (\/  /_
  \,.->._    \X-=/^
  (  /   `-._//^`
   `Y-.____(__}
    |     {__)
          ()
"""

player = Player("Brace", room["outside"])

directions = ["north", "east", "south", "west"]
direction_attr = {"north": "n_to", "east": "e_to", "south": "s_to", "west": "s_to"}
incomplete_actions = {
    "go": "Go where? Please specify north, east, south, or west.",
    "take": "Take what?",
}


def Check_Direction(direction):
    if direction.casefold() in directions:
        return direction
    else:
        return False


def Move_Player(player, direction):
    valid_dir = Check_Direction(split_inp[0])
    if not valid_dir:
        print("Not a valid direction, adventurer.")
        return
    else:
        next_room = getattr(player.current_room, direction_attr[valid_dir])
        if next_room == None:
            print(f"You cannot go {valid_dir} from here.")
            return
        else:
            player.current_room = next_room
            print(f"{next_room}")


print(f"\u001b[38;5;190m{titlecard}\033[0m")
print(f"\n{player.current_room}")

while True:
    inp = input("> ").casefold().strip()
    cur_items = player.current_room.items

    if "quit" in inp or inp == "q":
        print("Safe travels, adventurer")
        break

    split_inp = inp.split(" ", 1)

    if len(split_inp) < 2:
        action = split_inp[0]
        valid_dir = Check_Direction(action)
        if valid_dir:
            Move_Player(player, valid_dir)
        elif action == "who" or action == "character":
            print(avatar)
            print(
                f"You are {color.BLUE}{color.BOLD}{player.name}{color.END}, fearless adventurer of the Py Dungeon!"
            )
        elif action == "where":
            print(f"{player.current_room}")
        elif action == "look":
            print(f"{player.current_room}")
            list_items = "\n".join([str(item) for item in player.current_room.items])
            print("In this room you see:")
            print(list_items)
        else:
            print(incomplete_actions.get(action, f"{action} what now?"))
    elif len(split_inp) > 1:
        action, subject = split_inp[0], split_inp[1]
        if action == "go":
            Move_Player(player, subject)

