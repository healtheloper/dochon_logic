from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
result = []
max_val = -1

def bfs(graph, start, visited, count):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        count += 1
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return count

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(1,n+1):
    visited = [False] * (n+1)
    val = bfs(graph, i, visited, 0)
    result.append((i, val))
    max_val = max(max_val, val)

for item in result:
    if item[1] == max_val:
        print(item[0], end=" ")

