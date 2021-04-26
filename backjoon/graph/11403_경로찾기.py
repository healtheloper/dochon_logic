n = int(input())
arr = []
INF = int(1e9)
for i in range(n):
    data = list(map(int, input().split(" ")))
    arr.append(data)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            arr[i][j] = INF
for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])
for i in range(n):
    for j in range(n):
        if arr[i][j] != INF:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
