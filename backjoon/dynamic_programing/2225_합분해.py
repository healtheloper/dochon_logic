
n, k = map(int, input().split())
dp = [[1 for _ in range(201)] for _ in range(201)]
for i in range(1, len(dp)):
    dp[i][2] = i+1
for i in range(1, len(dp)):
    # k = 3
    # 20 3 -> 20 2 + 19 2 + 18 2 + ... + 1 2 + 0 2
    # if k = 4 이면 k = 3 일때 , 4 일때 ..

    # i = 1
    # d[1][3] = dp[1][2] + dp[0][2]

    # i = 2
    # d[2][3] = dp[2][2] + d[1][3]
    # d[3][3] = dp[3][2] + d[2][3]
    for j in range(3, k+1):
        dp[i][j] = dp[i][j-1]+dp[i-1][j]
print(dp[n][k])