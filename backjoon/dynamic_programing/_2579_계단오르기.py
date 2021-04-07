import copy
n = int(input())
arr = []
d = [[]] * (n)
for _ in range(n):
    arr.append(int(input()))

# d[0] = d[1] + d[2]
# d[1] = d[3]
# d[2] = d[3] + d[4]

# d[0], 10 = 1
## 시작 -> 0
### -> 1

# d[1], 20 = d[0] + 1 = 2
## 시작 -> 1, 시작 -> 0 -> 1
### -> 2

# d[2], 15 = 2
## d[1] + d[0] ?
## d[0] = 시작 -> 0 -> 2
## d[1] = 시작 -> 1 -> 2 , 시작 -> 0 -> 1 -> 2 (x)

### -> 2

# d[3], 25 = 2
## d[1] + d[2] ? 
### d[1] = 시작 -> 1 -> 3, 시작 -> 0 -> 1 -> 3
### d[2] = 시작 -> 1 -> 2 -> 3 (X), 시작 -> 0 -> 2 -> 3
### -> 3
count = 0
d[0] = [[0]]
d[1] = [[1], [0,1]]
# d[2] = [[0,1,2], [0,2], [1,2]]
for i in range(2, n):
    temp_arr = []
    temp_d = []
    for j in d[i-2]:
        temp_arr = copy.deepcopy(j)
        if j[len(j)-1] + 1 == i and j[len(j)-2]+1 != j[len(j)-1]:
            temp_arr.append(j[len(j)-1] + 1)
            temp_d.append(temp_arr)
        elif j[len(j)-1]+2 == i:
            temp_arr.append(j[len(j)-1] + 2)
            temp_d.append(temp_arr)
    for k in d[i-1]:
        temp_arr = copy.deepcopy(k)
        if k[len(k)-1] + 1 == i and k[len(k)-2]+1 != k[len(k)-1]:
            temp_arr.append(k[len(k)-1] + 1)
            temp_d.append(temp_arr)
        elif k[len(k)-1]+2 == i:
            temp_arr.append(k[len(k)-1] + 2)
            temp_d.append(temp_arr)
    temp_d = set(map(tuple, temp_d))
    for item in temp_d:
        d[i].append(list(item))

answer = 0
for array in d[n-1]:
    result = 0
    for idx in array:
        result += arr[idx]
    if answer < result:
        answer = result
print(answer)