import re
import sys
input = sys.stdin.readline

n = int(input())

pat = re.compile('(666)+')
arr = [0]
i = 666

while len(arr) <= n:
    if pat.search(str(i)) != None:
        arr.append(i)
    i += 1
print(arr[n])