from collections import deque
n= int(input())
INF = int(1e9)
arr = []
result = 0
cnt_arr = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    arr.append(list(map(int,input())))

def bfs(i, j):
    queue = deque([[i, j]])
    cnt = 0
    while queue:
        v = queue.popleft()
        a, b = v[0], v[1]
        arr[a][b] = 0
        cnt += 1
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0<=x<n and 0<=y<n and arr[x][y] == 1:
                queue.append([x, y])
                arr[x][y] = 0
    cnt_arr.append(cnt)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            result += 1
            bfs(i, j)
print(result)
cnt_arr.sort()
for i in cnt_arr:
    print(i)