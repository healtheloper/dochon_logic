x = input()

width = int(x)
squareNum = 0

a = int(width / 2) # (1x2) 이 들어갈 수 있는 개수
b = width % 2 # width가 홀수, 짝수일 때 구분

def factorial(num):
  fact = 1
    
  for i in range(1,num+1): 
      fact = fact * i 
  return fact
      

if ( b == 0) :
  for i in range(a):
    numA = a-i
    numB = i*2
    if(numB == 0):
      squareNum += 2 # 모두 a(1x2) 나 b(2x1)) 로 채워질 때
    else:
      parent = numA+numB
      squareNum += factorial(parent) // factorial(numA) // factorial(numB)
  print(int(squareNum) % 10007)

elif( b == 1) :
  squareNum = 1 # 모두 b(2x1)로 채워질 때
  for i in range(a):
    numA = a-i
    numB = i*2 + 1
    parent = numA+numB
    squareNum += factorial(parent) // factorial(numA) // factorial(numB)
  print(int(squareNum) % 10007)