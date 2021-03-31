
move = list(map(str, input()))
x_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = 0
y = int(move[1])
count = 0
for idx, value in enumerate(x_arr):
    if value == move[0]:
        x = idx+1
        break
dx = [-1, -2, -1, -2, 1, 2, 1, 2]
dy = [2, 1, -2, -1, 2, 1, -2, -1]

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx > 8 or ny > 8 or nx < 1 or ny < 1:
        continue
    count += 1
print(count)
