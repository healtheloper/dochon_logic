import string
alphabet = list(map(str, string.ascii_uppercase))

word = input()
count = 0
for i in range(len(word)):
    num = alphabet.index(word[i])
    if num < 3:
        count += 3
    elif 3 <= num < 6:
        count += 4
    elif 6 <= num < 9:
        count += 5
    elif 9 <= num < 12:
        count += 6
    elif 12 <= num < 15:
        count += 7
    elif 15 <= num < 19:
        count += 8
    elif 19 <= num < 22:
        count += 9
    elif 22 <= num < 26:
        count += 10
print(count)