import itertools
import sys
input = sys.stdin.readline
s = input().rstrip()
result = 0
all_s = set(itertools.permutations(s, len(s)))
for str in all_s:
    len_str = 0
    for idx in range(len(str)-1):
        if str[idx] != str[idx+1]:
            len_str += 1
        else:
            break
    if len_str == len(s)-1:
        result += 1
print(result)