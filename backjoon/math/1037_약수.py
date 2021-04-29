n = int(input())
if n == 1:
    m = int(input())
    print(m ** 2)
else:
    data = list(map(int, input().split(" ")))
    data.sort()
    print(data[0]*data[-1])
