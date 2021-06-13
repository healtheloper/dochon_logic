n = int(input())
datas = list(map(int, input().split()))
result = 0

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
for data in datas:
    if isPrime(data):
        result += 1
print(result)