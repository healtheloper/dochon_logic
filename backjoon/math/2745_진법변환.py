a, b = input().split()
b = int(b)
result = 0
for i in range(len(a)):
    try:
        if int(a[i]):
            result += a[i]*(b**(len(a)-i-1))
    except:
        result += (ord(a[i])-55)*(b**(len(a)-i-1))
print(result)

# enumerate 를 이용하여 풀었을 경우가 메모리 초과 X
# a[i] 로 사용하면 왜 메모리 초괴? 