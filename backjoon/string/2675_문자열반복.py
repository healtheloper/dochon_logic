t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)
    s = list(map(str, s))
    for char in s:
        for _ in range(r):
            print(char, end="")
    print()