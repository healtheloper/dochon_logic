a, b, c = map(int, input().split())
count = 0
# 2000 10 100
# 2010 100
# 2020 200
# 2100 1000
# 2200 2000
# 2230 2300 -> 23

# while a+(b*count) >= c*count:
#     if b >= c:
#         count = -1
#         break
#     count += 1
if c-b >= 1:
    count = a // (c-b) + 1
else:
    count = -1
print(count)
