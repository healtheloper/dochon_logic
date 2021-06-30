a, b = map(int, input().split())

data = list(map(int, input().split()))
result = 0
for floor in range(1, a+1):
    temp = []
    for item in data:
        if item >= floor:
            temp.append("X")
        else:
            temp.append("O")
    count_start = False
    prev_item = ''
    temp_count = 0
    for item in temp:
        if item == 'X' and count_start == False:
            count_start = True
            prev_item = item
        elif item == 'X' and count_start == True and prev_item == 'O':
            result += temp_count
            temp_count = 0
            prev_item = item
        elif item == 'X' and count_start == False and prev_item == 'X':
            continue
        if item == 'O' and count_start == True:
            temp_count += 1
            prev_item = item
print(result)