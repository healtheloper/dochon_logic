import math
n = int(input())

l = 0
r = 2**63

while l<=r:
    mid = (l+r)//2
    if mid**2 > n:
        r = mid-1
    elif mid**2 < n:
        l = mid+1
    else:
        l = mid
        break
print(l)