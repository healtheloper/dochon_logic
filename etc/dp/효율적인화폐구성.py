n, m = map(int,input().split())
#n 가지 종류의 화폐로 m원이 되도록 함
d = [10001]*(m+1)
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)
d[0] = 0

# 0, 1, 2
for i in range(n):
        
    for j in range(arr[i], m+1):
        print(j - arr[i], j, arr[i])
        if d[j - arr[i]] != 10001:
            d[j] = min(d[j], d[j-arr[i]]+1)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])