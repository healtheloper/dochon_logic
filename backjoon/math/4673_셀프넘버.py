number = 999
arr_numbers = []
arr_const = []
for item in range(1,number+1):
    arr_numbers.append(item)
    value = item
    thou = item // 1000
    value %= 1000
    hund = value // 100
    value %= 100
    ten = value // 10
    value %= 10
    one = value
    constructor = 0
    if thou > 0:
        constructor = item + thou + hund + ten + one
    elif hund > 0:
        constructor = item + hund + ten + one
    elif ten > 0:
        constructor = item + ten + one
    else:
        constructor = item + one
    arr_const.append(constructor)
for item in arr_const:
    if item in arr_numbers:
        arr_numbers.remove(item)
for item in arr_numbers:
    print(item)