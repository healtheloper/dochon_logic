N=4
S=[1, 2, 3]
d = [0] * (N+1)

d[0] = 0

for coin in S:
    for i in range(1, N+1):
        # coin = 1, 2, 3
        # i = 1, 2, 3, 4
        if coin == i:
            print(coin)
            d[i] += 1
            # 2 > 1
        elif i > coin:
            #d[2] += d[1]
            #d[3] += d[2]
            #d[4] += d[3]

            #d[3] += d[1]
            #d[4] += d[2]

            #d[4] += d[1]
            print(d[i], i, i-coin, d[i-coin])
            d[i] += d[i-coin]
print(d)