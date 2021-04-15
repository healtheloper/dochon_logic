n, k = map(int, input().split())
arr = []
INF = int(1e9)
for _ in range(n):
    arr.append(int(input()))
d = [INF] * (100001)
d[0] = 0

for coin in arr:
    for i in range(1, k+1):
        if coin == i:
            d[i] = 1
        elif i > coin:
            d[i] = min(d[i], d[i-coin]+1)

print(d[k] if d[k] != INF else -1)