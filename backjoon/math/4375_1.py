while True:
    try:
        n= int(input())
    except EOFError:
        break
    find_val = 1
    if n == 1:
        print(1)
        continue
    while True:
        if find_val % n == 0:
            print(len(str(find_val)))
            break
        else:
            find_val = find_val*10 + 1