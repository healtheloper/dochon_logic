n = int(input())
datas = list(map(int, input().split()))
# 1, 3, 1, 5

d = [0] * (100)

# 1
d[0] = datas[0]
# max(1, 3) = 3, 1을 터는 경우
d[1] = max(datas[0], datas[1])
for i in range(2, n):
    # d[2] = max(d[1], d[0]+datas[2]) = max(3, 1+1) = 3
    # 0, 2 를 터는게 효율적? 1을 터는게 효율적? -> 1을 터는것

    # d[3] = max(d[2], d[1]+datas[3]) = max(3, 3+5) = 8
    
    # d[2] = 이전 까지의 최적의 값(i-1, i-2)를 사용하여 다음 최적의 값을 찾음 
    # 1을 터는게 효율적? 1, 3을 터는게 효율적? 1, 3 -> 1, 3을 터는 것
    d[i] = max(d[i-1], d[i-2] + datas[i])
print(d[n-1])

