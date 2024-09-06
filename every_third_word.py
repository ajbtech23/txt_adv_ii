def third_word(arr_strings):
    arr_confirmed_third_word = []
    arr_confirmed_not_third_word = []
    for i in range(len(arr_strings)):
        if ((i + 1)) % 3 == 0:
            arr_confirmed_third_word.append((f"At position {i + 1} with index location {i} we have {arr_strings[i]} - a third word"))
        else:
            arr_confirmed_not_third_word.append((f"At position {i + 1} with index locatio {i} we have {arr_strings[i]} - not a third word"))

    for statement in arr_confirmed_third_word:
        print(statement)

    print("")

    for statement in arr_confirmed_not_third_word:
        print(statement)

arr_test = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta']

third_word(arr_test)
