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

def get_user_cmd():
    return input("Press 'Q' to quit the calculator otherwise lets have some fun with math XD")

def machine_calculator():

    user_is_active = True

    while user_is_active:
        user_cmd = get_user_cmd()

        if user_cmd in ['q', 'Q', 'quit', 'Quit']:
            print("All done for the day :D No more math hahaha")
            user_is_active = False
        else:
            arr_user_int_values = get_user_int_values()
