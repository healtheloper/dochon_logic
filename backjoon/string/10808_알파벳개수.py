import string
alphabet = list(map(str, string.ascii_lowercase))
arr = [0] * 26
input_data = input()
for i in input_data:
    arr[alphabet.index(i)] += 1
print(' '.join(list(map(str, arr))))