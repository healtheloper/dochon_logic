
V, E = map(int, input().split())
INF = int(1e9)
dist = [[INF for _ in range(V+1)] for _ in range(V+1)]

for _ in range(E):
    start, end, d = map(int, input().split())
    dist[start][end] = d

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j])

min_cycle = INF
for i in range(1, V+1):
    min_cycle = min(min_cycle, dist[i][i])
    
if min_cycle == INF: 
    print(-1)
else:
    print(min_cycle)