S = int(input())
def chk(mid):
    return mid*(mid+1)/2 > S
l = 1
r = 93000# math.sqrt(4294967295*2)

while (l<=r):
    mid = (l+r) // 2
    if chk(mid):
        r=mid-1
    else:
        l=mid+1
print(r)