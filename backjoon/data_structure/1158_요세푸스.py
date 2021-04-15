n, k = map(int, input().split())
arr = []
result = []
for i in range(n):
    arr.append(i+1)

idx = 0
while arr:
    idx += k-1
    if idx > len(arr)-1:
        idx %= len(arr)
    result.append(arr.pop(idx))

print("<" + str(result)[1:-1]+">")