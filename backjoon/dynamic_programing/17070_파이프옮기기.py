import copy
n = int(input())
arr = []
for i in range(n):
    datas = list(map(int, input().split()))
    arr.append(datas)
front = [1,2]
back = [1,1]
count = 0
def right(arr, front, back):
    new_front = copy.deepcopy(front)
    new_back = copy.deepcopy(back)
    new_back[0], new_back[1] = new_front[0], new_front[1]
    new_front[1] += 1
    bfs(arr, new_front, new_back)

def down(arr, front, back):
    new_front = copy.deepcopy(front)
    new_back = copy.deepcopy(back)
    new_back[0], new_back[1] = new_front[0], new_front[1]
    new_front[0] += 1
    bfs(arr, new_front, new_back)

def diagonal(arr, front, back):
    new_front = copy.deepcopy(front)
    new_back = copy.deepcopy(back)
    new_back[0], new_back[1] = new_front[0], new_front[1]
    new_front[0] += 1
    new_front[1] += 1
    bfs(arr, new_front, new_back)

def bfs(arr, front, back):
    new_front = copy.deepcopy(front)
    new_back = copy.deepcopy(back)
    global count
    if new_front[0] == n and new_front[1] == n:
        count += 1
        return
    temp_a = new_front[0]
    temp_b = new_front[1]
    isRightWall, isRightWall, isDiagWall = 1, 1, 1
    if temp_b < n:
        isRightWall = arr[temp_a-1][temp_b]
    if temp_a < n:
        isDownWall = arr[temp_a][temp_b-1]
    if temp_a < n and temp_b < n:
        isDiagWall = arr[temp_a][temp_b] + arr[temp_a][temp_b-1] + arr[temp_a-1][temp_b]
    if new_front[0] == new_back[0] and temp_b < n:
    # 가로면
        # 오
        if isRightWall == 0:
            right(arr, new_front, new_back)
        # 대
        if isDiagWall == 0:
            diagonal(arr, new_front, new_back)
    elif new_front[1] == new_back[1] and temp_a < n:
    # 세로면
        # 아
        if isDownWall == 0:
            down(arr, new_front, new_back)
        # 대
        if isDiagWall == 0:
            diagonal(arr, new_front, new_back)
    elif temp_a < n and temp_b < n:
    # 대각선이면
        # 오
        if isRightWall == 0:
            right(arr, new_front, new_back)
        # 아
        if isDownWall == 0:
            down(arr, new_front, new_back)
        # 대
        if isDiagWall == 0:
            diagonal(arr, new_front, new_back)
bfs(arr, front, back)
print(count)