n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
result = []
max_val = -1
def dfs(x):
    if visited[x] == True:
        return
    visited[x] = True
    dfsArray.append(x)
    for i in graph[x]:
        dfs(i)
        
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(1, n+1):
    dfsArray = []
    visited = [False] * (n+1)
    dfs(i)
    max_val = max(max_val, len(dfsArray))
    result.append((i, len(dfsArray)))
for item in result:
    if item[1] == max_val:
        print(item[0], end=" ")

