from abc import abstractproperty


data = input().split(".")
check = True
arr = []
while check:
    for item in data:
        total_len = len(item)
        if total_len == 0:
            arr.append(".")
            continue
        while total_len > 0:
            if total_len % 2 == 1:
                check = False
                break
            if total_len > 3:
                total_len -= 4
                arr.append("AAAA")
            elif total_len > 1:
                total_len -= 2
                arr.append("BB")
        arr.append(".")
    break
arr.pop()
if check == True:
    print(''.join(arr))
else:
    print(-1)