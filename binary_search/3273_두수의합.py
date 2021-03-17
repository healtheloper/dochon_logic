n = int(input())
data = list(map(int, input().split()))
x = int(input())

data.sort()
count = 0

for i in data:
    low = 0
    high = len(data)-1
    result = 0
    while low<=high:
        mid = (low+high)//2
        if i + data[mid] == x:
            count += 1
            break
        elif i + data[mid] < x:
            low = mid+1
        else:
            high = mid-1
print(count//2)