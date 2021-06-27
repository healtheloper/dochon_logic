n, k = map(int, input().split())
arr = []
for i in range(1, k+1):
    result = str(n*i)
    result = result[::-1]
    arr.append(int(result))
arr.sort(reverse=True)
print(arr[0])
