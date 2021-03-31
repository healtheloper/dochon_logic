a, b = map(int, input().split())
count = 0
while a>1:
    if a % b == 0:
        a = a//b
        count += 1
    else:
        a -= 1
        count += 1

print(count)