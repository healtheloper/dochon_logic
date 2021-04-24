from collections import deque
n, m = map(int, input().split())
arr = []
count = 0
tomato = []
for _ in range(m):
    data = list(map(int, input().split(" ")))
    arr.append(data)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(tomato):
    global count
    q = deque([tomato])
    while q:
        v = q.popleft()
        temp_q = []
        for item in v:
            a, b = item[0], item[1]
            for k in range(4):
                x = a + dx[k]
                y = b + dy[k]
                if 0<=x<m and 0<=y<n and arr[x][y] == 0:
                    temp_q.append([x, y])
                    arr[x][y] = 1
        if len(temp_q) > 0:
            count += 1
            q.append(temp_q)

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            tomato.append((i, j))

bfs(tomato)

check = True
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            check = False
if check:
    print(count)
else:
    print(-1)