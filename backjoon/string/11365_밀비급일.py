
while True:
    sentence = list(input())
    if ''.join(sentence) == "END":
        break
    sentence.reverse()
    print(''.join(sentence))