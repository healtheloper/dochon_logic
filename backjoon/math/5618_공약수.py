n = int(input())
count = 1
arr=[]
max_val = 0
if n == 2:
    a, b = map(int, input().split(" "))
    if b > a:
        a, b = b, a
    while b!= 0:
        n = a%b
        a = b
        b = n
    max_val = a
if n == 3:
    data = list(map(int, input().split(" ")))
    data.sort()
    a, b, c = data[0], data[1], data[2]
    while a!=0:
        n = b%a
        b = a
        a = n
    while b!=0:
        m = c%b
        c = b
        b = m
    max_val = c
# 125 % 75 = 50 : n, a : 75, b: 50
# 75 % 50 = 25 : n, a: 50, b:25
# 50 % 25 = 0 a = 25 -> 최대공약수


for i in range(1, max_val+1):
    if max_val % i == 0:
        arr.append(i)
for _ in arr:
    print(_)