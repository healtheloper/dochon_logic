num = int(input())
d = [0] * (num+1)

if num == 1:
    print(0)
elif num == 2:
    print(1)
else:
    d[1], d[2], d[3] = 0, 1, 1

    for i in range(4, num+1):
        if i % 2 == 0 and i % 3 == 0:
            d[i] = min(d[i//2], d[i//3], d[i-1]) + 1
        elif i % 2 == 0:
            d[i] = min(d[i//2], d[i-1]) + 1
        elif i % 3 == 0:
            d[i] = min(d[i//3], d[i-1]) + 1 
        else:
            d[i] = d[i-1] + 1
    print(d[num])

### best

# num = int(input())
# d = [0] * (10**6+1)

# for i in range(2, num+1):
#     d[i] = d[i-1] + 1

#     if i % 2 == 0:
#         d[i] = min(d[i], d[i//2]+1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i//3]+1)
    
# print(d[num])