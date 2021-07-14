import itertools
n = int(input())
datas = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
min_val = int(1e9)
max_val = -int(1e9)
arr = ["+" for _ in range(plus)] + ["-" for _ in range(minus)]
arr += ["*" for _ in range(mul)]
arr += ["/" for _ in range(div)]

nPr = list(itertools.permutations(arr, n-1))
for item in nPr:
    result = 0
    for idx in range(len(datas)):
        if idx == 0:
            result += datas[idx]
            continue
        if item[idx-1] == "+":
            result += datas[idx]
        elif item[idx-1] == "-":
            result -= datas[idx]
        elif item[idx-1] == "*":
            result *= datas[idx]
        elif item[idx-1] == "/":
            if result < 0:
                result *= -1
                result //= datas[idx]
                result *= -1
            else:
                result //= datas[idx]
    min_val = min(result, min_val)
    max_val = max(result, max_val)
print(max_val)
print(min_val)