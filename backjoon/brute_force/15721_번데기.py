a = int(input())
t = int(input())
c = int(input())

result_count = 0
count = 2
result = 0
ok = True
while ok:
    command = [0, 1, 0, 1]
    command += [0 for _ in range(count)]
    command += [1 for _ in range(count)]
    for item in command:
        if item == c:
            result_count += 1
            if result_count == t:
                ok=False
                break
        result += 1
    count += 1
print(result%a)
