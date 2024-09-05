def get_user_sports_goods():
    return input("What pair of sneakers would you like to purchase today?\n")

def is_len_of_arr_odd(arr_sports_goods):
    if (len(arr_sports_goods) % 2) == 0:
        return False
    else:
        return True

def calc_middle_index_of_arr(arr_sports_goods):
    return int(((len(arr_sports_goods) + 1) / 2)) - 1


def play():

    arr_sports_goods = []
    user_still_active = True

    while user_still_active:
        user_selected_sports_good = get_user_sports_goods()

        if user_selected_sports_good in ['q', 'Q', 'quit', 'Quit']:
            print("Thank you for shopping with us today; we look forward to seeing you again soon :D")
            user_still_active = False
        else:
            print(f"Those {user_selected_sports_good} will look great on you!")
            arr_sports_goods.append(user_selected_sports_good)

    print("\nLet's take a look at all of the items in your basket :D\n")

    i = 0
    for sports_good in arr_sports_goods:
        print(f"{i + 1}. {sports_good}")
        i += 1

    if is_len_of_arr_odd(arr_sports_goods):
        middle_index_of_arr = calc_middle_index_of_arr(arr_sports_goods)
        print(f"\nYou have won the {arr_sports_goods[middle_index_of_arr]} and can take them home for free XD")
    else:
        print("\nNo soup for you!")




play()
