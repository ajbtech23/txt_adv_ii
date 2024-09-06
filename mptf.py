# Multiplication tables from 1 to 5

def calc_multiples():
    for x in range(1, 6):
        print(f"\nThese are the multiplcations for {x} between 1 to 12:\n")
        for y in range(1, 13):
            print(f"{x} multiplied by {y} gives us {x * y}")

def calc_factors():
    for x in range(1, 13):
        arr_confirmed_factors = []
        print("")
        for y in range(1, x + 1):
            if x % y == 0:
                print(f"{y} is a factor of {x}")
                arr_confirmed_factors.append(y)
            else:
                print(f"{y} is not a factor of {x}")

        print(f"These are all of the confirmed factors of {x}:")
        i = 0
        for z in arr_confirmed_factors:
            print(f"{i + 1}. ==> {z}")
            i += 1

calc_factors()
