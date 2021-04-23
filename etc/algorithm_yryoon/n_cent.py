N=10
S=[2, 3, 5, 6]
d = [0] * (N+1)
d[0] = 0

for coin in S:
    for i in range(1, N+1):
        if coin == i:
            d[i] += 1
        elif i > coin:
            d[i] += d[i-coin]
print(d[N])