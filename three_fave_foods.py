def get_user_food_option():
    return input("What is dish is a personal fave of yours?\n")

arr_fave_foods = []
i = 0

while i < 3:
    print("")
    user_selected_food_option = get_user_food_option()
    arr_fave_foods.append(user_selected_food_option)
    i += 1

print("")
for index, food in enumerate(arr_fave_foods, 1):
    print(f"{index}. ==> {food}")
