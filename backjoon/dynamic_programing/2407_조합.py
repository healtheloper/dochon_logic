n, m = map(int, input().split())

d = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(min(i+1, m+1)):
        if i == j or j==0:
            d[i][j] = 1
        else:
            d[i][j] = d[i-1][j] + d[i-1][j-1]
print(d[n][m])