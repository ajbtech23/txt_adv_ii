favorites = []
more_items = True

while more_items:
    user_input = input("Add something to your shopping basket:\n")

    if user_input == '':
        print("\nThank you for shopping with us :D")
        more_items = False
    else:
        print(f"\nThose {user_input} you bought will look amazing this Spring!")
        favorites.append(user_input)


print("Here are all of the lovely things you have bought today:\n")
for index, fave in enumerate(favorites, 1):
    print(f"{index}. ==> {fave}")
