n = int(input())
result = []

for num in range(n+1):
    arr = []
    result_num = num
    temp_num = num
    while(num>=10):
        arr.append(num%10)
        num //= 10
    arr.append(num%10)
    for item in arr:
        result_num += item
    if result_num == n:
        result.append(temp_num)
if len(result)>0:
    print(result[0])
else:
    print(0)
