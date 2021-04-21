import math
n = int(input())
INF = int(1e9)
d = [INF for _ in range(n+1)]
for i in range(n+1):
    if math.sqrt(i)*10%10 == 0:
        d[i] = 1
    else:
        near = math.floor(math.sqrt(i))
        for j in range(1, near+1):
            near_double = j**2
            d[i] = min(d[i], d[near_double] + d[i-near_double])
print(d[n])