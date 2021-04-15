n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
d = [0] * (N+1)
d[0] = 0

for coin in S:
    for i in range(1, N+1):
        if coin == i:
            d[i] += 1
        elif i > coin:
            d[i] += d[i-coin]
print(d[N])