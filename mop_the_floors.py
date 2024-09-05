def pretty_print(arr):
    for item in arr:
        print(f"*. {item}")
    print("\nThank you for shopping with us :D!")

favorites = []
more_items = True

def prettier_print(arr):
    i = 0
    for item in arr:
        print(f"{i + 1}. {item}")
        i += 1
    print("\nYou look oh so fly XD")

def prettier_still(arr):
    for i in range(len(arr)):
        print(f"{i + 1}. ==> {arr[i]}")
    print("\nThey almost had me but I hustled my way through...\n")

def prettiest_print(arr):
    for index, element in enumerate(arr, 1):
        print(f"{index}... {element}")
    print("\nNikes on my feet keep my cypher complete :D\n")


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

print("")
pretty_print(favorites)
print("")
prettier_print(favorites)
print("")
prettier_still(favorites)
print("")
prettiest_print(favorites)
