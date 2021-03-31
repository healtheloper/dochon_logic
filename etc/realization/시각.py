n = int(input())

count = 0

for i in range(n+1):
    if i % 10 == 3:
        count += 60*60
    else:
        count += (15*60) + (45*15)

print(count)