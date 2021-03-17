n = int(input())
data = list(map(int, input().split()))
x = int(input())

data.sort()
count = 0

for i, v in enumerate(data):
    for j in range(n-i-1):
        if v + data[n-1-j] == x:
            data = data[i+1:n-j-2]
            count += 1
            break
print(count)
    