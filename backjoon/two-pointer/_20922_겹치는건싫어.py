n, k = map(int, input().split())
arr = list(map(str, input().split()))
dict = {}
result = -1

def find(idx):
    dict = {}
    count = 0
    global result
    for i in range(idx, len(arr)):
        item = arr[i]
        try:
            dict[item] += 1
            if dict[item] > k:
                result = max(result, count)
                first_idx = arr.index(item)
                find(first_idx+1)
                return
            count += 1
        except:
            dict[item] = 1
            count += 1
find(0)
print(result)