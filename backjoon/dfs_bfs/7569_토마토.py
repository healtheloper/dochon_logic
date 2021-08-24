from collections import deque

n, m, h = map(int, input().split())
arr = []
floor = []
count = 0
tomato = []
for _ in range(m*h):
    data = list(map(int, input().split(" ")))
    floor.append(data)
    if len(floor) == m:
        arr.append(floor)
        floor = []

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]
def bfs(tomato):
    global count
    q = deque([tomato])
    while q:
        v = q.popleft()
        temp_q = []
        for item in v:
            a, b, c = item[0], item[1], item[2]
            for k in range(6):
                z = a + dh[k]
                x = b + dy[k]
                y = c + dx[k]
                if 0<=x<m and 0<=y<n and 0<=z<h and arr[z][x][y] == 0:
                    temp_q.append([z, x, y])
                    arr[z][x][y] = 1
        if len(temp_q) > 0:
            count += 1
            q.append(temp_q)

for i in range(h):
    for j in range(m):
        for k in range(n):
            if arr[i][j][k] == 1:
                tomato.append((i, j, k))
bfs(tomato)
check = True
for i in range(h):
    for j in range(m):
        for k in range(n):
            if arr[i][j][k] == 0:
                check = False
if check:
    print(count)
else:
    print(-1)