n, m = map(int, input().split())

result = 0
for _ in range(n):
    datas = list(map(int, input().split()))
    datas.sort()
    min_value = datas[0]
    result = max(min_value, result)

print(result)