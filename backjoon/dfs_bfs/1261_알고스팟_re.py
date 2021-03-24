import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
maps = [[] for _ in range(m)]
for _ in range(m):
    rows = input()
    for i in range(len(rows)-1):
        maps[_].append(int(rows[i]))
ch = [[-1]*n for _ in range(m)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()
q.append((0, 0))
ch[0][0] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < m and 0<= ny < n:
            if ch[nx][ny] == -1:
                if maps[nx][ny] == 0:
                    ch[nx][ny] = ch[x][y]
                    q.appendleft((nx, ny))
                else:
                    ch[nx][ny] = ch[x][y] + 1
                    q.append((nx,ny))
print(ch[m-1][n-1])

