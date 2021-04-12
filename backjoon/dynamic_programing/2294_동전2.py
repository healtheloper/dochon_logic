n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
d = [0] * (k+1)
d_dict = {}
d[0] = 0

for i in range(1, k+1):
    d_dict[i] = []
for idx in range(len(arr)):
    for i in range(1, k+1):
        if arr[idx] == i:
            d[i] += 1
        elif i > arr[idx]:
            d[i] += d[i-arr[idx]]
            if idx == len(arr)-1 and i == k:
                print(d[i-arr[idx]])
            