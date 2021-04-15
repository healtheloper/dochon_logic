INF = int(1e9)
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)
nearest = [0] * (v+1)
visited = [False] * (v+1)
set_of_edges = [1]
result = 0

# 양방향 트리 연결
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
# 초깃값 설정 (v1 에서 출발)
for ed in graph[1]:
    nearest[ed[0]] = 1
    distance[ed[0]] = ed[1]
    
for i in range(2, v+1):
    min = INF
    for i in range(2, v+1):
        if distance[i]<min and visited[i] != True:
        #if distance[i]<min and i not in set_of_edges: -> 시간초과
            min = distance[i]
            vnear = i
    set_of_edges.append(vnear)
    result += distance[vnear]
    visited[vnear] = True
    for ed in graph[vnear]: 
        if ed[1] < distance[ed[0]]:
            distance[ed[0]] = ed[1]
            nearest[ed[0]] = vnear
print(result)
