N = int(input())
A = list(map(int,input().split()))
M = int(input())
data = list(map(int,input().split()))

# def binary_search(arr, value, high, low):
#     arr.sort()
#     if low > high:
#         print(0)
#         return
#     mid = (low+high)//2
#     if arr[mid] == value:
#         print(1)
#         return
#     if arr[mid] > value:
#         high = mid-1
#         binary_search(arr, value, high, low)
#     elif arr[mid] < value:
#         low = mid+1
#         binary_search(arr, value, high, low)
A.sort()
for i in data:
    low = 0
    high = len(A)-1
    result = 0
    while low<=high:
        mid = (low+high) // 2
        if A[mid] > i:
            high = mid-1
        elif A[mid] <= i:
            if result < mid:
                result = mid
            low = mid+1
    if A[result] == i:
        print(1)
    else:
        print(0)