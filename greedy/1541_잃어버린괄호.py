a = input()

minus_arr = a.split("-")
result = 0

for i in range(len(minus_arr)):
  plus_arr = map(int, minus_arr[i].split("+"))
  plus_val = sum(plus_arr)
  if(i==0):
    result += plus_val
  else:
    result -= plus_val
print(result)