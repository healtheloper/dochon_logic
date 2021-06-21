import sys
def compare(str1, str2):
    x = 0
    for i in range(len(str2)):
        if str2[i] == str1[x]:
            x += 1
            if x == len(str1):
                return "Yes"
    return "No"

while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    a, b = line.split()
    print(compare(a, b))