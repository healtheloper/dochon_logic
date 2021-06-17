check = True
while check:
    data = list(map(int, input().split()))
    if data.count(0) == 3:
        check = False
        break
    data.sort(reverse=True)
    bigV, s1, s2 = data[0], data[1], data[2]
    if bigV ** 2 == s1**2+s2**2 and bigV > 0 and s1 > 0 and s2 > 0:
        print("right")
    else:
        print("wrong")