bfsArray = []
queue = []

#간선, 노드 설정
node = input()
a, b = input().split(" ")
edge = input()

if int(a) > int(b):
  start = b
  end = a
else :
  start = a
  end = b

node = int(node)
edge = int(edge)
start = int(start)
end = int(end)

visited = [0]*(node)
obj = {}

for item in range(node):
  obj[item+1] = []
for item in range(edge):
  m = input()
  x, y = m.split(" ")
  x = int(x)
  y = int(y)
  obj[x].append(y)
  obj[y].append(x)

for item in range(node):
  obj[item+1].sort()

#bfs
def bfs(x):
  visited[x-1] = 1;
  queue.append(x)
  level = 1
  while len(queue) > 0:
    front = queue.pop(0);
    bfsArray.append(front)
    for item in obj[front]:
      if(visited[item-1] == 0):
        if(item == end):
          print(level)
          break;
        visited[item-1] = 1
        queue.append(item)
    level += 1
    
bfs(start);