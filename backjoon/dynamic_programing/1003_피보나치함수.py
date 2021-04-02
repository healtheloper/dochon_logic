# fibo(0) = 1 0
# fibo(1) = 0 1
# fibo(2) = 1 1
# fibo(3) = 1 2
# fibo(4) = 2 3
n = int(input())
d = [(0,0)]*(41)
d[0] = (1,0)
d[1] = (0,1)
def dp(num):
    if d[num] != (0,0):
        return d[num]
    d[num] = (dp(num-2)[0] + dp(num-1)[0], dp(num-2)[1] + dp(num-1)[1])
    return d[num]
for _ in range(n):
    m = int(input())
    print(dp(m)[0], dp(m)[1])

