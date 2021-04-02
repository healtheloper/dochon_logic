import sys
num = int(input())
sys.setrecursionlimit(10**6)
d = [0] * (num+1)
def dp(num):
    if num == 2 or num == 3:
        d[num] = 1
        return d[num]
    if d[num] != 0:
        return d[num]
    if num % 2 == 0 and num % 3 == 0:
        d[num] = min(dp(num//2), dp(num//3), dp(num-1)) + 1
    elif num % 2 == 0:
        d[num] = min(dp(num//2), dp(num-1)) + 1
    elif num % 3 == 0:
        d[num] = min(dp(num//3), dp(num-1)) + 1
    else:
        d[num] = dp(num-1) + 1
    return d[num]
dp(num)

print(d[num])
