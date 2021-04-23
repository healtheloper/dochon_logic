from collections import deque
n, m = map(int, input().split())
INF = int(1e9)
arr = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    arr.append(list(map(int,input())))

def bfs(graph):
    visited = [False] * (m+1)
    queue = deque([[0, 0]])
    while queue:
        v = queue.popleft()
        a, b = v[0], v[1]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0<=x<n and 0<=y<m and arr[x][y] == 1:
                queue.append([x, y])
                arr[x][y] = arr[a][b] + 1
bfs(arr)
print(arr[n-1][m-1])
# def move(x, y, count):
#     if x == m and y == n:
#         print(count)
#         return
#     if x+1 != m:
#         if arr[x+1][y] == 1:
#             count += 1
#             move(x+1, y, count)
#     if y+1 != n:
#         if arr[x][y+1] == 1:
#             count += 1
#             move(x, y+1, count)
#     if x-1 > 0:
#         if arr[x-1][y] == 1:
#             count += 1
#             move(x-1, y, count)
#     if y-1 > 0:
#         if arr[x][y-1] == 1:
#             count += 1
#             move(x, y-1, count)
# move(0,0,0)