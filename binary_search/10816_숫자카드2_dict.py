N = int(input())
A = list(map(int,input().split()))
M = int(input())
have_arr = list(map(int,input().split()))

result_dict = {}

for i in A:
    if i in result_dict:
        result_dict[i] += 1
    else:
        result_dict[i] = 1
print(result_dict)
print(' '.join(str(result_dict[m]) if m in result_dict else '0' for m in have_arr))