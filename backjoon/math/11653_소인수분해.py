n = int(input())

def divide(n):
    for i in range(2, n+1):
        if n % i == 0:
            print(i)
            divide(n//i)
            return
divide(n)