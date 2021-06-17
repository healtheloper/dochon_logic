check = True
while check:
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    bigV, s1, s2 = data
    if bigV ** 2 == s1**2+s2**2:
        print("right")
    else:
        print("wrong")
    if data.count(0) == 3:
        check = False