num = int(input())
d = [0] * (10**6+1)
arr = [num]
for i in range(2, num+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
def dp(num):
    if num == 1:
        return
    if num % 2 == 0 and num % 3 == 0:
        min_val = min(d[num//2], d[num//3], d[num-1])
        if d[num//2] == min_val:
            arr.append(num//2)
            dp(num//2)
        elif d[num//3] == min_val:
            arr.append(num//3)
            dp(num//3)
        elif d[num-1] == min_val:
            arr.append(num-1)
            dp(num-1)
    elif num % 2 == 0:
        if d[num//2] > d[num-1]:
            arr.append(num-1)
            dp(num-1)
        else:
            arr.append(num//2)
            dp(num//2)
    elif num % 3 == 0:
        if d[num//3] > d[num-1]:
            arr.append(num-1)
            dp(num-1)
        else:
            arr.append(num//3)
            dp(num//3)
    else:
        arr.append(num-1)
        dp(num-1)
dp(num)
print(d[num])
for item in arr:
    print(item, end=" ")
