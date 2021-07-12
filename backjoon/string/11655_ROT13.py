import string
i = input()
up = list(string.ascii_uppercase)
low = list(string.ascii_lowercase)

for ch in i:
    if ch in up:
        print(up[(up.index(ch)+13)%26], end="")
    elif ch in low:
        print(low[(low.index(ch)+13)%26], end="")
    else:
        print(ch, end="")
