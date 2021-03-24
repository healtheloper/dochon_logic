a = list(map(int, input()))
a.sort()

if(a[0] != 0):
  print("-1")
else:
  if(sum(a) % 3 == 0):
    a.reverse()
    for i in a:
      print(i, end="")
  else:
    print("-1")