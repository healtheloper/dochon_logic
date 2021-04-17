arr = []
max_len = -1
for _ in range(5):
    string = input()
    if max_len < len(string):
        max_len = len(string)
    arr.append(list(map(str, string)))

for i in range(max_len):
    for j in range(5):
        try:
            print(arr[j][i], end="")
        except:
            continue