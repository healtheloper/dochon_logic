n, m, k = map(int, input().split())
datas = list(map(int, input().split()))
datas.sort(reverse=True)

big_one = datas[0]
big_two = datas[1]
count = 0
result = 0
for _ in range(m):
    if count < k:
        result += big_one
        count += 1
    else:
        result += big_two
        count = 0
print(result)