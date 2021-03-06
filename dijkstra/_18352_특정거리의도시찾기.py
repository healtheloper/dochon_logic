# 도시의 개수 N 도로의 개수 M 거리 정보 K 출발 도시 X

import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, K, X = map(int, input().split())

graph = [[] for i in range(N+1)]
visited = [False] * (N+1)
distance = [INF] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        #1 => 2, 3
        #distance[2] [3] = 1
        distance[i] = 1
    for i in range(N-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + 1
            if cost < distance[j]:
                distance[j] = cost
dijkstra(X)

visited = [False] * N
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        visited[i-1] = True

if True not in visited:
    print(-1)
    