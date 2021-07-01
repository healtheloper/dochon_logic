t = int(input())

for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    print(min(data), max(data))