words = input().split(" ")
for i in words:
    if len(i) == 0:
        words.remove(i)

if words == ['']:
    print(0)
else:
    print(len(words)) 