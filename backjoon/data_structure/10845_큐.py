import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        cmd_value = command[1]
        arr.append(cmd_value)
    elif command[0] == 'pop':
        if len(arr) > 0:
            pop_value = arr[0]
            arr = arr[1:]
            print(pop_value)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(arr))
    elif command[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'back':
        if len(arr) > 0:
            print(arr[len(arr)-1])
        else:
            print(-1)
    elif command[0] == 'front':
        if len(arr) > 0:
            print(arr[0])
        else:
            print(-1)
