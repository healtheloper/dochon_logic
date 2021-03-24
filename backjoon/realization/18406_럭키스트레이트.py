# 점수 N이 10이상 1억이하, 자릿수는 항상 짝수

a = input()
sum_1=0
sum_2=0

for idx, item in enumerate(a):
  if(idx < len(a)/2):
    sum_1 += int(item)
  else:
    sum_2 += int(item)

if(sum_1 == sum_2):
  print("LUCKY")
else:
  print("READY")