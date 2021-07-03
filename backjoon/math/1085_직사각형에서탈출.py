a, b, c, d = map(int, input().split())
print(min(min(a, c-a), min(b, d-b)))