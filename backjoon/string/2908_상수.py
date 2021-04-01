a, b = map(str, input().split())
a = list(map(str, a))
b = list(map(str, b))

a.reverse()
b.reverse()

a = int(''.join(a))
b = int(''.join(b))

if a > b:
    print(a)
else:
    print(b)