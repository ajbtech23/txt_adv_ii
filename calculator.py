def calc_sum(x, y):
    return (x + y)

def calc_difference(x, y):
    return (x - y)

def calc_product(x, y):
    return (x * y)

def calc_div_output(x, y):
    return (x / y)

def calc_exponents_output(x, y):
    return (x ** y)

def get_user_int_values():
    arr_user_int_values = []
    i = 0

    while i < 2:
        arr_user_int_values.append(int(input("Please provide a value to use in your calculation:\n")))
        i += 1
    return arr_user_int_values

def get_user_calc_choice():
    return input("Would you like to add, subtract, multiply or divide? You can also use this as a chance to close the app...\n")

def get_user_cmd():
    return input("Press 'Q' to quit the calculator or press 'GO' and lets 'GO' have some fun with math XD\n")

def machine_calculator():

    user_is_active = True

    while user_is_active:
        user_cmd = get_user_cmd()

        if user_cmd in ['q', 'Q', 'quit', 'Quit']:
            print("All done for the day :D No more math hahaha")
            user_is_active = False
        else:
            arr_user_int_values = get_user_int_values()
            str_user_calc_choice = get_user_calc_choice()

            if str_user_calc_choice == 'add':
                print(f"The sum of {arr_user_int_values[0]} and {arr_user_int_values[1]} is {calc_sum(arr_user_int_values[0], arr_user_int_values[1])}")
            elif str_user_calc_choice == 'subtract':
                print(f"The difference between {arr_user_int_values[0]} and {arr_user_int_values[1]} is {calc_difference(arr_user_int_values[0], arr_user_int_values[1])}")
            elif str_user_calc_choice == 'multiply':
                print(f"The product of {arr_user_int_values[0]} and {arr_user_int_values[1]} is {calc_product(arr_user_int_values[0], arr_user_int_values[1])}")
            elif str_user_calc_choice == 'divide':
                print(f"The output from the division of {arr_user_int_values[0]} by {arr_user_int_values[1]} is {calc_div_output(arr_user_int_values[0], arr_user_int_values[1])}")
            elif str_user_calc_choice == 'exponents':
                print(f"The output of applying {arr_user_int_values[1]} is an exponent onto the base {arr_user_int_values[0]} is {calc_exponents_output(arr_user_int_values[0], arr_user_int_values[1])}")
            else:
                print("Try again...")

machine_calculator()
