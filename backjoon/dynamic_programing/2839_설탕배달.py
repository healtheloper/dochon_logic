# 01

n = int(input())
arr = [3, 5]
INF = int(1e9)
d = [INF] * (5001)
d[3] = 1
d[5] = 1
for kg in arr:
    for i in range(1, n+1):
        d[i] = min(d[i], d[i-kg]+1)
print(d[n] if d[n] != INF else -1)