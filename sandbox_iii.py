arr_insert = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
arr_arrs_values = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], arr_insert, [-1, -2, -3], [-23], True, False]

max_arr_size = 0
largest_arr = None

for arr in arr_arrs_values:
    try:
        if len(arr) > max_arr_size:
            largest_arr = arr
            max_arr_size = len(arr)
    except TypeError:
        print(f"The value that was passed in {arr} does not return an output when passed through len()")

print(largest_arr)
