from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
m = int(input())
visited = [False]*(n+1)
count = 0
def bfs(graph, start, visited, count):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        count += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return count

# 양 방향으로 추가 필요
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(graph, 1, visited, count)-1)
