dfsArray = []
bfsArray = []
queue = []

#간선, 노드 설정
data = input()
a, b, c = data.split(" ")
a = int(a)
b = int(b)
c = int(c)

visited = [0]*(a)
obj = {}
for item in range(a):
  obj[item+1] = []
for item in range(b):
  m = input()
  x, y = m.split(" ")
  x = int(x)
  y = int(y)
  obj[x].append(y)
  obj[y].append(x)

for item in range(a):
  obj[item+1].sort()

#dfs
def dfs(x):
  visited[x-1] = 1;
  dfsArray.append(x);
  for item in obj[x]:
    if(visited[item-1] == 0):
      dfs(item)

#bfs
def bfs(x):
  visited[x-1] = 1;
  queue.append(x)
  while len(queue) > 0:
    front = queue.pop(0);
    bfsArray.append(front)
    for item in obj[front]:
      if(visited[item-1] == 0):
        visited[item-1] = 1
        queue.append(item)

#c부터 dfs
dfs(c);
#visited 초기화
visited = [0]*(a)

#c부터 bfs
bfs(c)

for item in dfsArray:
  print(item, end=" ");
print()
for item in bfsArray:
  print(item, end=" ");