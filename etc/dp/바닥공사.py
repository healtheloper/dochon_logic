n = int(input())
# 2 x N 크기의 바닥을 채우는 바닥의 수를 796,796으로 나눈 나머지를 출력
d = [0] * 1001

d[1] = 1
d[2] = 3
# d[3] = 5
# d[4] = 2x2 + 2x1 xd[2] + 
for i in range(3, n+1):
    d[i] = (d[i-1] + 2 * d[i-2]) % 796796
print(d[n-1])