from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque([])
for _ in range(n):
    datas = input().split()
    if datas[0] == "push":
        q.append(datas[1])
    elif datas[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif datas[0] == "size":
        print(len(q))
    elif datas[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif datas[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    elif datas[0] == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])
