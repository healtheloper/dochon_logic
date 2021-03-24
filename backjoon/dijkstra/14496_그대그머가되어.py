import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
dijkstra(a)

if distance[b] != INF: 
    print(distance[b])
else:
    print(-1)