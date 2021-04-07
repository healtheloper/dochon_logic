n = int(input())
INF = int(1e9)
coin_type = [2, 5]
d = [0]*(10 ** 6 + 1)
d[1] = -1
for coin in coin_type:
    d[coin] = 1
for i in range(2, n+1):
    if i-5 >= 0:
        result = INF
        for coin in coin_type:
            if d[i-coin] != -1 and d[coin] != -1:
                min_val = d[i-coin] + d[coin]
                result = min(result, min_val)
                d[i] = result
        if d[i] == 0:
            d[i] = -1
    else:
        if d[i-2] != -1:
            d[i] = d[i-2] + d[2]
        else:
            d[i] = -1
print(d[n])