from itertools import combinations
import copy
# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2

col, row = map(int, input().split())
arr = [[0 for _ in range(row)] for _ in range(col)]
temp_arr = [[0 for _ in range(row)] for _ in range(col)]

count = 0
virus = []
wall = []
safety = []
#1, 5, arr
def breedVirus(x, y, arr):
  # for item in arr:
  #   print(item)
  # print("============")
  #R
  if y < row-1:
    if arr[x][y+1] == 0:
      arr[x][y+1] = 2
      breedVirus(x, y+1, arr)
  #L
  if y > 0:
    if arr[x][y-1] == 0:
      arr[x][y-1] = 2
      breedVirus(x, y-1, arr)
  #U
  if x < col-1:
    if arr[x+1][y] == 0:
      arr[x+1][y] = 2
      breedVirus(x+1, y, arr)
  #D
  if x > 0:
    if arr[x-1][y] == 0:
      arr[x-1][y] = 2
      breedVirus(x-1, y, arr)

def checkSafeArea():
  areaCount = 0
  for i in range(col):
    for j in range(row):
      if arr[i][j] == 0:
        areaCount += 1
  return areaCount

for i in range(col):
  count = 0
  data = input().split()
  for item in data:
    arr[i][count] = int(item)
    temp_arr[i][count] = int(item)
    if(int(item) == 2):
      virus.append((i, count))
    elif(int(item) == 1):
      wall.append((i, count))
    else:
      safety.append((i, count))
    count += 1

#1을 놓는 경우의 수
# safety[0] [1] [2]
# len(safety) 3개를 뽑는 조합
safety_count = []
for item in range(len(safety)):
  safety_count.append(item)
comb_safety = list(combinations(safety_count, 3))

result = 0

# [((0,0) (0,1) (0,2)), ]
for item in comb_safety:
  # 조합으로 지정한 safety 배열 내 점 3개
  one = item[0]
  two = item[1]
  three = item[2]
  # safety의 0번째 배열 (0, 0) 의 row [0]
  # safety의 0번째 배열 (0, 0) 의 col [1]
  if(arr[safety[one][0]][safety[one][1]] == 1
  or arr[safety[two][0]][safety[two][1]] == 1
  or arr[safety[three][0]][safety[three][1]] == 1):
    continue
  arr[safety[one][0]][safety[one][1]] = 1
  arr[safety[two][0]][safety[two][1]] = 1
  arr[safety[three][0]][safety[three][1]] = 1
  for item in virus:
    x = item[0]
    y = item[1]
    breedVirus(x,y,arr)
  temp = checkSafeArea()
  if(result < temp):
    result = temp
  arr = copy.deepcopy(temp_arr)

print(result)