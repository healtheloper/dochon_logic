a = int(input())
arr = []
for i in range(a):
    datas = list(map(int, input().split()))
    grade_sum = 0
    grade_count = len(datas)-1
    avr_count = 0
    for grade in range(1, len(datas)):
        grade_sum += datas[grade]
    grade_aver = grade_sum / grade_count
    for grade in range(1, len(datas)):
        if datas[grade] > grade_aver:
            avr_count += 1
    arr.append((avr_count/grade_count)*100)

for item in arr:
    print(f"{item:.3f}%")