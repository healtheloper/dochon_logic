num = int(input())
num_set = set()
m = num
for _ in range(num):
    word = input()
    for i in range(len(word)):
        if word[i] not in num_set:
            num_set.add(word[i])
        elif word[i-1] == word[i]:
            continue
        else:
            m -= 1
            break
    num_set = set()
print(m)
