import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
maps = [[] for _ in range(m)]
for _ in range(m):
    rows = input()
    for i in range(len(rows)-1):
        maps[_].append(int(rows[i]))

graph = [[] for _ in range(n*m+1)]
distance = [INF] * (n*m+1)
for i in range(1, n*m+1):
    # 좌표가 (n, m) 일 때
    if (i//n) == (m) and i%n == 0:
        continue
    # 좌표가 (a, m) 일 때
    elif (i//n) == (m-1) and i%n != 0:
        graph[i].append((i+1, maps[i//n][i%n]))
    # 좌표가 (n, b) 일 때
    elif (i % n) == 0:
        graph[i].append((i+n, maps[i//n][n-1]))
    else:
        graph[i].append((i+1, maps[i//n][i%n]))
        graph[i].append((i+n, maps[i//n+1][i%n-1]))
def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))
dijkstra(1)

print(distance[n*m])
