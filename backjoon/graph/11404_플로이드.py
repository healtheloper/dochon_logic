def print_arr(d):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if d[i][j] != INF:
                print(d[i][j], end=" ")
            else:
                print(0, end=" ")
        print()

n = int(input())
m = int(input())
INF = int(1e9)
d = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    d[a][b] = min(d[a][b], c)

for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==j:
                d[i][j] = 0
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])
print_arr(d)