class Axe:
    def __init__(self):
        self.name = "Battle Axe"
        self.description = "it is the weapon of legend... wield with great care..."

    def __str__(self):
        return f"This is {self.name}; {self.description}"

class LongSword:
    def __init__(self):
        self.name = "Long Sword"
        self.description = "perfect for close quarter combat... one swing will surely turn all who stand against you into stains on the pavement"

    def __str__(self):
        return f"This is {self.name}; {self.description}"

class Gauntlets:
    def __init__(self):
        self.name = "Gauntlets"
        self.description = "battle tested and guaranteed to fell even the strongest of foes"

    def __str__(self):
        return f"{self.name}; {self.description}"



def get_user_instruction():
    return input("What would you like to do Sailor?\n")

def play():
    arr_item_inventory = [Axe(), LongSword(), Gauntlets()]
    bool_user_is_active = True

    print("Welcome to Dressrosa - try to make it out alive XD")
    while bool_user_is_active:
        str_user_instruction = get_user_instruction()

        if str_user_instruction in ['q', 'Q', 'quit', 'Quit']:
            print("Travel safe Sailor... tis treacherous waters ye face...")
            bool_user_is_active = False
        elif str_user_instruction in ['n', 'N', 'north', 'North', '^']:
            print("Ye will be travelling North!")
        elif str_user_instruction in ['e', 'E', 'east', 'East', '>']:
            print("Ye will be travelling East!")
        elif str_user_instruction in ['s', 'S', 'south', 'South', 'v']:
            print("Ye will be travelling South!")
        elif str_user_instruction in ['w', 'W', 'west', 'West', '<']:
            print("Ye will be travelling West!")
        elif str_user_instruction in ['i', 'I', 'inventory', 'Inventory']:
            print("You have access to the following items in your inventory:\n")
            i = 0
            for item in arr_item_inventory:
                print(f"{i + 1}. ==> {item}")
            print("Choose one... and conquer the world!\n")
        else:
            print("Ye cannot be understood... try again Sailor...")

play()
