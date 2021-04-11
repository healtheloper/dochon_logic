n = int(input())
for _ in range(n):
    arr = []
    output_break = False
    input_data = input()
    for i in input_data:
        if i == "(":
            arr.append(i)
        else:
            if not arr:
                print("NO")
                output_break = True
                break
            else:
                arr.pop()
    if output_break != True:
        if not arr:
            print("YES")
        else:
            print("NO")