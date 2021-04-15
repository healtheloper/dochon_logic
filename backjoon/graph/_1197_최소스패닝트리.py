# Minimum Spanning Tree
# 모든 정점들을 연결하는 부분 그래프 중에서 가중치의 합이 최소인 트리

# Trim
# nearest
# distance
INF = int(1e9)
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)
nearest = [0] * (v+1)
set_of_edges = [1]
result = 0
W = [[INF for _ in range(v+1)] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    W[a][b] = c
    W[b][a] = c

for i in range(2, v+1):
    nearest[i] = 1
    distance[i] = W[1][i]

for i in range(2, v+1):
    min = INF
    print(distance)
    for i in range(2, v+1):
        if distance[i]<min:
            min = distance[i]
            vnear = i
    set_of_edges.append(vnear)
    result += distance[vnear]
    distance[vnear] = INF
    for j in range(2, v+1):
        if j not in set_of_edges:
            distance[j] = W[j][vnear]
            nearest[j] = vnear
print(result)
print(set_of_edges)

# Kruskal
# 덩어리로 (disjoint subset)