s = input()
arr = []
for idx in range(len(s)):
    arr.append(s[idx:])
arr.sort()
for item in arr:
    print(item)