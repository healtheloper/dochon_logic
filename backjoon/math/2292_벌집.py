# 1 7 19 37 61
#  6 12 18 24
# 1 = 1
# 1과 7사이 수 -> 2
# 8과 19 사이 수 -> 3
n = int(input())
temp = 1
count = 0
while True:
    if temp >= n:
        break
    temp += count*6
    count += 1
if n == 1:
    print(1)
else: 
    print(count)