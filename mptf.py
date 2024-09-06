# Multiplication tables from 1 to 5

for x in range(1, 6):
    print(f"\nThese are the multiplcations for {x} between 1 to 12:\n")
    for y in range(1, 13):
        print(f"{x} multiplied by {y} gives us {x * y}")
