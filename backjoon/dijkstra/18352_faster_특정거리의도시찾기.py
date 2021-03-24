# 도시의 개수 N 도로의 개수 M 거리 정보 K 출발 도시 X
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, K, X = map(int, input().split())

graph = [[] for i in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

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
dijkstra(X)

visited = [False] * N
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        visited[i-1] = True

if True not in visited:
    print(-1)
    