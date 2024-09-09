def calc_total(arr_values):
    return (arr_values[0] + arr_values[1])

def calc_diff(arr_values):
    return (arr_values[0] - arr_values[1])

def calc_prod(arr_values):
    return (arr_values[0] * arr_values[1])

def calc_divd(arr_values):
    return (arr_values[0] / arr_values[1])

def calc_powr(arr_values):
    return (arr_values[0] ** arr_values[1])

def play():

    user_calc_active = True

    while user_calc_active:
        str_user_calc_status = input("\nWelcome to CalcuME; would you like to use the calculator? Enter 'YES' to proceed and anything else to exit:\n> ")
        if str_user_calc_status.lower() == 'yes':
            arr_values = []

            while len(arr_values) < 2:
                try:
                    user_input_value = int(input("Give us a number:\n> "))
                    arr_values.append(user_input_value)
                except ValueError:
                    print(f"Your last input will not work in our calculator... try again!")

            print("You have given us the following values to work with:\n")
            for val in arr_values:
                print(f"We will be working with: {val}")

            print("What calculation would you like to perform? You can:\n Add; Subtract; Multiply; Divide; Calculate the results from an 'Exponent' application... Enter 'Q' to quit...")
            user_calc_choice = input("Your choice is:\n> ")

            if user_calc_choice in ['q', 'Q', 'quit', 'Quit']:
                print("Thanks for playing :D ta ta!")
                user_calc_active = False
            elif user_calc_choice == 'Add':
                print(f"The sum of {arr_values[0]} and {arr_values[1]} is {calc_total(arr_values)}")
            elif user_calc_choice == 'Subtract':
                print(f"The difference between {arr_values[0]} and {arr_values[1]} is {calc_diff(arr_values)}")
            elif user_calc_choice == 'Multiply':
                print(f"The product of {arr_values[0]} and {arr_values[1]} is {calc_prod(arr_values)}")
            elif user_calc_choice == 'Divide':
                print(f"The resulting output from the division of {arr_values[0]} and {arr_values[1]} is {calc_divd(arr_values)}")
            elif user_calc_choice == 'Exponents':
                print(f"The resulting output from applying {arr_values[1]} as an exponent onto {arr_values[0]} is {calc_powr(arr_values)}")
            else:
                print("We couldn't make sense of your chosen calculation I'm afraid...")
        else:
            print("It's been a pleasure; goodbye :D")
            user_calc_active = False


play()
