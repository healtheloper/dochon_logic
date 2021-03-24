N = int(input())
A = list(map(int,input().split()))
M = int(input())
have_arr = list(map(int,input().split()))

result_dict = {}
for i in have_arr:
    result_dict[i] = 0;

have_arr.sort()
for i in A:
    low = 0
    high = len(have_arr)-1
    result = -1
    while low<=high:
        mid = (low+high) // 2
        if have_arr[mid] <= i:
            if result < mid:
                result = mid
            low = mid+1
        elif have_arr[mid] > i:
            high = mid-1
    if have_arr[result] == i:
        result_dict[i] += 1

result = result_dict.values()
print(*result)
# for item in result:
#     print(item, end=" ")