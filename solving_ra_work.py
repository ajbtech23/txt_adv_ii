x = [1, 2, 3, 4, 5]

arr_elements_greater_than_three = []

for z in x:
    if z > 3:
        arr_elements_greater_than_three.append(z)
    else:
        continue

print("The following elements in the array provided are greater than 3:\n")

i = 0
for y in arr_elements_greater_than_three:
    print(f"{i+1} ==> {y}")
    i += 1
