
n, m = map(int, input().split())

def prime_list(n, m):
    sieve = [True] * (m+1)
    x = int(m**0.5)
    for i in range(2, x+1):
        if sieve[i] == True:
            for j in range(i+i, m+1, i):
                sieve[j] = False
    if n == 1:
        n=2
    return [i for i in range(n, m+1) if sieve[i] == True]

arr = prime_list(n, m)
for item in arr:
    print(item)