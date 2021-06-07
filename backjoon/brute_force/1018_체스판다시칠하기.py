n, m = map(int, input().split())

arr = []
result = int(1e9)

for i in range(n):
    data = list(input())
    arr.append(data)
dx = m-8 # 5
dy = n-8 # 2


for x in range(dx+1):
    for y in range(dy+1):
        count = 0
        else_count = 0
        first_word = arr[y][x]
        if first_word == "B":
            second_word = "W"
        else:
            second_word = "B"
        for i in range(y, 8+y):
            for j in range(x, 8+x):
                if (i-y)%2 == 0 and (j-x)%2 == 0:
                    if arr[i][j] != first_word:
                        count += 1
                    else:
                        else_count += 1
                elif (i-y)%2 == 0 and (j-x)%2 == 1:
                    if arr[i][j] != second_word:
                        count += 1
                    else:
                        else_count += 1
                elif (i-y)%2 == 1 and (j-x)%2 == 0:
                    if arr[i][j] != second_word:
                        count += 1
                    else:
                        else_count += 1
                elif (i-y)%2 == 1 and (j-x)%2 == 1:
                    if arr[i][j] != first_word:
                        count += 1
                    else:
                        else_count += 1
        result = min(count, result, else_count)
        
print(result)
