import sys

input = sys.stdin.readline
INF = int(1e9)
n = int(input())
datas = list(map(int, input().split()))
m = int(input())
isDatas = list(map(int, input().split()))
data_dict = {}
result_arr = [0] * m
for idx, value in enumerate(isDatas):
    data_dict[value] = idx

isDatas.sort()
result = -1
for data in datas:
    result = -1
    low = 0
    high = len(isDatas)-1
    result_index = 0
    # isDatas = -10, -5, 2, 3, 4, 5, 9 , 10
    while low<=high:
        middle = (low+high) // 2
        if data < isDatas[middle]:
            high = middle-1
        elif data >= isDatas[middle]:
            if result < middle:
                result = middle
            low = middle+1
    if isDatas[result] == data:
        try:
            result_index = data_dict[isDatas[result]]
        except:
            result_index = 0
        result_arr[result_index] += 1
for _ in result_arr:
    print(_, end=" ")