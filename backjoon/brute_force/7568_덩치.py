n = int(input())
arr = []
for _ in range(n):
    new_count = 1
    a, b = map(int, input().split())
    for item in arr:
        kg, m, count = item[0], item[1], item[2]
        if kg > a and m > b:
            new_count += 1
        if kg < a and m < b:
            item[2] += 1
    arr.append([a,b,new_count])
for item in arr:
    print(item[2], end=" ")