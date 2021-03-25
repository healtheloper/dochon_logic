import sys

input = sys.stdin.readline

datas = list(map(str, input()))
datas.pop() # null 제거

cursor_index = len(datas)

m = int(input())
for _ in range(m):
    cmd = input().split()
    if cmd[0] == 'P':
        if cursor_index == len(datas):
            datas.append(cmd[1])
            cursor_index += 1
        else:
            tmp = datas[:cursor_index]
            tmp.append(cmd[1])
            datas = datas[cursor_index:]
            tmp.extend(datas)
            datas = tmp
            cursor_index += 1
    if cmd[0] == 'L':
        if cursor_index > 0:
            cursor_index -= 1
    if cmd[0] == 'D':
        if cursor_index < len(datas):
            cursor_index += 1
    if cmd[0] == 'B':
        if cursor_index > 0:
            if cursor_index == len(datas):
                datas.pop()
                cursor_index -= 1
            else:
                tmp = datas[:cursor_index-1]
                datas = datas[cursor_index:]
                tmp.extend(datas)
                datas = tmp
                cursor_index -= 1
print(''.join(datas))