def get_user_cmd():
    return input("What would you like to do Sailor?\n")

def play():
    items = ['Great Axe', 'Silver(5)', 'Apple']

    user_is_active = True

    print("Welcome to Greed Island -_____-\n")

    while user_is_active:

        user_cmd = get_user_cmd()

        if user_cmd in ['n', 'N', 'north', 'North', '^']:
            print("We are travelling North!")
        elif user_cmd in ['e', 'E', 'east', 'East', '>']:
            print("We are travelling East!")
        elif user_cmd in ['s', 'S', 'south', 'South', 'v']:
            print("We are travelling South!")
        elif user_cmd in ['w', 'W', 'west', 'West', '<']:
            print("We are travelling West!")
        elif user_cmd in ['i', 'I', 'inventory', 'INVENTORY']:
            print("\nYou have access to the following items in your inventory:\n")
            i = 1
            for item in items:
                print(f"{i}. ==> {item}")
                i += 1
            print("")
        elif user_cmd in ['q', 'Q', 'quit', 'QUIT']:
            print("\nFare ye well Sailor for it is treacherous waters ye face...")
            user_is_active = False
        else:
            print("We cyant understand ye Sailor! Try again!!!!")

play()
