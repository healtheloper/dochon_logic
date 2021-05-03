
n = input()
arr = []
result = ""
n_len = len(n)
# 333,334
for i in range(n_len):
    if n[i] != '\n':
        toBinary = int(n[i])
    else:
        continue
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