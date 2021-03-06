x = input()

for i in range(int(x)):

  starNum = (int(x)-i)*2-1

  for k in range(i):
    print(" ", end='');
  for j in range(starNum):
    print("*", end='');
    
  print();