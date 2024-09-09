name = input("Please enter your name:\n> ")
age = input("Please enter your age:\n> ")
try:
    print(f"You were born in {(2024 - int(age))}")
except ValueError:
    print(f"We are unable to calculate the year you were born because '{age}' is not a number")
