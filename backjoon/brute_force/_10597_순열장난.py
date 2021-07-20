data = input()
arr = []
long_val = ''
print(data)
for idx in range(len(data)):
    in_val = data[idx]
    if not in_val in arr and long_val == '':
        arr.append(in_val)
    else:
        long_val += data[idx]
        if not long_val in arr:
            arr.append(long_val)
            long_val = ''
print(' '.join(arr))
#151413121110987123456