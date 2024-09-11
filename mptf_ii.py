for x in range(1, 11):
    arr_published_multiples = []
    for y in range(1, 11):
        arr_published_multiples.append(str(x*y))
    print(f"\nThese are the first 10 multiples of {x}:")
    print(", ".join(arr_published_multiples))

for x in range(1, 11):
    arr_published_factors = []
    arr_published_non_factors = []
    for y in range(1, x + 1):
        if x % y == 0:
            arr_published_factors.append(str(y))
        else:
            arr_published_non_factors.append(str(y))

    print(f"\nThese are the confirmed factors of {x}:")
    print(", ".join(arr_published_factors))

    if len(arr_published_non_factors) == 0:
        print(f"{x} has no non factors < than {x}")
    else:
        print(f"These are the values which are not factors of {x}:")
        print(f", ".join(arr_published_non_factors))
