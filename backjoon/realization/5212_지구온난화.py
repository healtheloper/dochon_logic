row, col = map(int, input().split())
arr = []
result_arr = []
for _ in range(row):
    data = list(map(str, input()))
    arr.append(data)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_row = -1
max_col = -1
min_row = int(1e9)
min_col = int(1e9)
for r in range(row):
    temp = []
    for c in range(col):
        sea_num = 0
        if arr[r][c] == "X":
            for i in range(4):
                if r+dx[i] < 0 or r+dx[i] == row or c+dy[i] == col or c+dy[i] < 0:
                    sea_num += 1
                elif arr[r+dx[i]][c+dy[i]] == ".":
                    sea_num += 1
            if sea_num >= 3:
                temp.append(".")
            else:
                temp.append("X")
                max_row = max(max_row, r)
                max_col = max(max_col, c)
                min_row = min(min_row, r)
                min_col = min(min_col, c)
        else:
            temp.append(".")
    result_arr.append(temp)

for i in range(min_row, max_row+1):
    for j in range(min_col, max_col+1):
        print(result_arr[i][j], end="")
    print()