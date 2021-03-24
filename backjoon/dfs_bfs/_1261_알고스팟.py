import sys
from itertools import permutations
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
maps = [[] for _ in range(m)]
for _ in range(m):
    rows = input()
    for i in range(len(rows)-1):
        maps[_].append(int(rows[i]))

count = n+m-2
moving_arr = []
for _ in range(n-1):
    moving_arr.append(1)
for _ in range(m-1):
    moving_arr.append(0)
moving_comb = list(set(permutations(moving_arr)))

result = INF
for move in moving_comb:
    x = 0
    y = 0
    count = 0
    # 0, 1, 0, 1
    for item in move:
        if item == 0:
            x += 1
            if maps[x][y] == 1:
                count += 1
        else:
            y += 1
            if maps[x][y] == 1:
                count += 1
    if count < result:
        result = count
print(result)

