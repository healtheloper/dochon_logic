n, m = map(int, input().split())
count = 0

if n==1 :
  count = 1
elif n==2 :
  if m <= 7 :
    count = 1 + (m-1)//2
  elif m > 7:
    count = 4
elif n>2:
  if m < 7 :
    count = min(m, 4)
  else:  
    count = m - 2

print(count)