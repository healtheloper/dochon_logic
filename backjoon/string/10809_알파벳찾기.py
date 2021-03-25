import string
alphabet = list(map(str, string.ascii_lowercase))

S = list(map(str, input()))

for item in alphabet:
    for idx, value in enumerate(S):
        if item == value:
            print(idx, end=" ")
            break
        else:
            if idx == len(S)-1:
                print(-1, end=" ")