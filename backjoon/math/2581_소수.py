n = int(input())
m = int(input())
result = 0
min_val = int(1e9)
def isPrime(num):
    if num < 2:
        return False
    count = 0
    for n in range(2, num+1):
        if num % n == 0:
            count += 1
        if count > 1:
            return False
    return True
for data in range(n, m+1):
    if isPrime(data):
        result += data
        min_val = min(result, min_val)

if result != 0:
    print(result)
    print(min_val)
else:
    print(-1)