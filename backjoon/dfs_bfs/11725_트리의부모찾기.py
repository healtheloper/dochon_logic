import sys
sys.setrecursionlimit(10**5)

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
dfsArray = []
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, parent):
    if visited[x] == True:
        return
    visited[x] = True
    dfsArray.append((x, parent))
    for i in graph[x]:
        if not visited[i]:
            dfs(i, x)
dfs(1, 0)
sorted_dfs = sorted(dfsArray, key=lambda x:x[0])

for i in range(1, len(sorted_dfs)):
    print(sorted_dfs[i][1])