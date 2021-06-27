a, b = input().split()
b = int(b)
result = 0
for i in range(len(a)):
    if a[i].isnumeric():
        result += a[i]*(b**(len(a)-i-1))
    else:
        result += (ord(a[i])-55)*(b**(len(a)-i-1))
print(result)