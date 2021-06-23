n = int(input())
words = set()
for _ in range(n):
    word = input()
    words.add(word)
words = sorted(list(words), key=lambda x:(len(x), x))

for word in words:
    print(word)