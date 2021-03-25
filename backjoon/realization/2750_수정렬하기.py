import sys

input = sys.stdin.readline

count = int(input())
arr = []
for _ in range(count):
    data = int(input())
    arr.append(data)
arr.sort()
for item in arr:
    print(item)