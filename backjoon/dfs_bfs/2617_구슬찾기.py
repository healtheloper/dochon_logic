import collections

n, m = map(int, input().split())
bead_u = {}
bead_d = {}

for _ in range(n):
  bead_u[_+1] = []
  bead_d[_+1] = []

for i in range(m):
  a, b = map(int, input().split())
  bead_u[a].append(b)
  bead_d[b].append(a)

result = 0
middle = (n+1)/2

def dfs_u(num):
  global result
  q = collections.deque()
  visited = [False for _ in range(n+1)]
  visited[num] = True
  q.append(num)
  count = 0

  while q:
    num = q.popleft()
    for i in bead_u[num]:
      if not visited[i]:
        visited[i] = True
        count += 1
        if count >= middle:
          result += 1
          return
        q.append(i)

def dfs_d(num):
  global result
  q = collections.deque()
  visited = [False for _ in range(n+1)]
  visited[num] = True
  q.append(num)
  count = 0

  while q:
    num = q.popleft()
    for i in bead_d[num]:
      if not visited[i]:
        visited[i] = True
        count += 1
        if count >= middle:
          result += 1
          return
        q.append(i)

for idx in range(n):
  dfs_u(idx+1)
  dfs_d(idx+1)

print(result)