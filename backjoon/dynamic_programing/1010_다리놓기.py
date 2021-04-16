t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    d = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == j:
                d[i][j] = 1
            elif i == 1:
                d[i][j] = j
            else:
                d[i][j] = d[i-1][j-1] + d[i][j-1]
    print(d[n][m])
