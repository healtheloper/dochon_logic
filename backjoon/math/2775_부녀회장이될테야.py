t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    arr = [0] * (n+1)
    for floor in range(k+1):
        if floor == 0:
            for i in range(1, n+1):
                arr[i] = i
        else:
            temp = [0] * (n+1)
            for i in range(1, n+1):
                for item in range(1, i+1):
                    temp[i] += arr[item]
            arr = temp
    print(arr[n])
