n, m = map(int, input().split())

a_arr = []
arr=[]
result = [[0]*m for _ in range(n)]
count = 0

for i in range(n):
  data = list(map(str, input().split()))
  for i in range(len(data[0])):
    arr.append(data[0][i])
  a_arr.append(arr)
  arr=[]

for j in range(n):
  data = list(map(str, input().split()))
  for i in range(len(data[0])):
    if(a_arr[j][i] == data[0][i]):
      result[j][i] = True
    else:
      result[j][i] = False

for i in range(len(result)-2):
  for j in range(len(result[i])-2):
    if(result[i][j] == False):  
      result[i][j] = not result[i][j]
      result[i][j+1] = not result[i][j+1]
      result[i][j+2] = not result[i][j+2]
      result[i+1][j] = not result[i+1][j]
      result[i+1][j+1] = not result[i+1][j+1]
      result[i+1][j+2] = not result[i+1][j+2]
      result[i+2][j] = not result[i+2][j]
      result[i+2][j+1] = not result[i+2][j+1]
      result[i+2][j+2] = not result[i+2][j+2]
      count += 1

for i in range(len(result)):
  for j in range(len(result[i])):
    if(result[i][j] == False):
      count = -1
      break;
      
print(count)