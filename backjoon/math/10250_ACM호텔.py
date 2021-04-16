t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    y = n % h if n%h!= 0 else h
    x = (n // h if n%h!=0 else n//h-1) + 1
    print(f"{y}{x if x>=10 else f'0{x}'}")