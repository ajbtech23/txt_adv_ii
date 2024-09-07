x = [1, 2,3, 4, 5]

arr_elements_greater_than_three = []

for y in x:
    if y > 3:
        arr_elements_greater_than_three.append(y)
    else:
        continue

print("These are all of the elements in the arr greater than 3:\n")

for index, element in enumerate(arr_elements_greater_than_three, 1):
    print(f"{index}. ==> {element}")
