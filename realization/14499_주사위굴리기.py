def move(direction):
    if direction == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif direction == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif direction == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif direction == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]

def xy(direction):
  if direction == 1: return 0, 1
  elif direction == 2: return 0, -1
  elif direction == 3: return -1, 0
  elif direction == 4: return 1, 0

n, m, x, y, k = map(int, input().split())
arr = []

for i in range(n):
  data = list(map(int, input().split()))
  arr.append(data)

moving = map(int, input().split())
dice = [0 for _ in range(7)]

for item in moving:
  a, b = xy(item)
  if 0<=x+a<n and 0<=y+b<m:
    x+=a
    y+=b
    move(item)
    if arr[x][y] != 0:
      dice[1] = arr[x][y]
      arr[x][y] = 0
    else:
      arr[x][y] = dice[1]
    print(dice[6])