import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    data = list(map(int, input().split()))
    arr.append(data)
k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())
    result = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            result += arr[a][b]
    print(result)