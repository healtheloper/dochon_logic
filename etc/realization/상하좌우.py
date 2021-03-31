n = int(input())
moves = list(map(str, input().split()))
x = 1
y = 1
for move in moves:
    if move == 'R':
        if x < n:
            x += 1
    elif move =='L':
        if x > 2:
            x -= 1
    elif move =='U':
        if y > 2:
            y -= 1
    elif move =='D':
        if y < n:
            y += 1
print(y, x)