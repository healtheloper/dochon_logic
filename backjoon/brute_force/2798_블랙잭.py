n, m = map(int, input().split())
datas = list(map(int, input().split()))
profit = 0

for i in range(len(datas)):
    for j in range(i, len(datas)):
        for k in range(j, len(datas)):
            if i==j or j==k or i==k:
                continue
            temp_profit = datas[i]+datas[j]+datas[k]
            if abs(m-profit) > abs(m-temp_profit) and m >= temp_profit:
                profit = temp_profit

print(profit)