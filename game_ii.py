def get_user_input():
    return input("What would you like to do next Sailor?\n")

def play():
    items_inventory = ['BattleAxe', 'Copper(23)', 'Beef Stew']
    user_active = True
    print("Welcome to Elbaf -_____- ==> can you make it out alive?!")
    while user_active:
        user_input = get_user_input()

        if user_input in ['q', 'Q', 'quit', 'Quit']:
            print("Travel safely Sailor... These be treacherous waters...")
            user_active = False
        elif user_input in ['n', 'N', 'north', 'North', '^']:
            print("We are travelling North!")
        elif user_input in ['e', 'E', 'east', 'East', '>']:
            print("We are travelling East!")
        elif user_input in ['s', 'S', 'south', 'South', 'v']:
            print("We are travelling South!")
        elif user_input in ['w', 'W', 'west', 'West', '<']:
            print("We are travelling West!")
        elif user_input in ['i', 'I', 'inventory', 'INVENTORY']:
            print("You have access to the following items in your inventory:\n")
            for index, item in enumerate(items_inventory, 1):
                print(f"{index}. ==> {item}")
        else:
            print("Try again Sailor... your diction be too brazy...")

play()
