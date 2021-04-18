n = input()
arr = []
result = ""
for i in range(len(n)):
    toBinary = int(n[i])
    temp = []
    count = 4
    for _ in range(3):
        quotient = toBinary // count
        toBinary %= count
        count //= 2
        temp.append(quotient)
    arr.append(temp)
for i in arr:
   result += ''.join(map(str, i))
print(int(result))