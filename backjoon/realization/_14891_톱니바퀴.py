import collections

def rotate_clock(cog_deq, direction):
  if direction == 1:
    x = cog_deq.pop()
    cog_deq.appendleft(x)
  elif direction == -1:
    x = cog_deq.popleft()
    cog_deq.append(x)
  return cog_deq
  
first_cog = input()
second_cog = input()
third_cog = input()
forth_cog = input()

first_deq = collections.deque(first_cog)
second_deq = collections.deque(second_cog)
third_deq = collections.deque(third_cog)
forth_deq = collections.deque(forth_cog)

def NS_check():
  magnets = [False for _ in range(3)]
  if first_deq[2] != second_deq[6]:
    magnets[0] = True
  if second_deq[2] != third_deq[6]:
    magnets[1] = True
  if third_deq[2] != forth_deq[6]:
    magnets[2] = True
  return magnets

def next_cog_check(magnets, cog_num):
  if magnets[cog_num-1]:
    return True
  else:
    return False

def cog_rotate(cog_num, direction):
  magnets = NS_check()
  global first_deq
  global second_deq
  global third_deq
  global forth_deq
  if cog_num == 1:
    first_deq = rotate_clock(first_deq, direction)
    if magnets[0]:
      direction *= -1
      second_deq = rotate_clock(second_deq, direction)
      if magnets[1]:
        direction *= -1
        third_deq = rotate_clock(third_deq, direction)
        if magnets[2]:
          direction *= -1
          forth_deq = rotate_clock(forth_deq, direction)
  elif cog_num == 2:
    second_deq = rotate_clock(second_deq, direction)
    if magnets[0]:
      direction *= -1
      first_deq = rotate_clock(first_deq, direction)
    if magnets[1]:
      direction *= -1
      third_deq = rotate_clock(third_deq, direction)
      if magnets[2]:
        direction *= -1
        forth_deq = rotate_clock(forth_deq, direction)
  elif cog_num == 3:
    third_deq = rotate_clock(third_deq, direction)
    if magnets[1]:
      direction *= -1
      second_deq = rotate_clock(second_deq, direction)
      if magnets[0]:
        direction *= -1
        first_deq = rotate_clock(first_deq, direction)
    if magnets[2]:
      direction *= -1
      forth_deq = rotate_clock(forth_deq, direction)
  elif cog_num == 4:
    forth_deq = rotate_clock(forth_deq, direction)
    if magnets[2]:
      direction *= -1
      third_deq = rotate_clock(third_deq, direction)
      if magnets[1]:
        direction *= -1
        second_deq = rotate_clock(second_deq, direction)
        if magnets[0]:
          direction *= -1
          first_deq = rotate_clock(first_deq, direction)

result = 0

def cog_check(first_deq, second_deq, third_deq, forth_deq):
  global result
  if first_deq[0] == "1":
    result += 1
  if second_deq[0] == "1":
    result += 2
  if third_deq[0] == "1":
    result += 4
  if forth_deq[0] == "1":
    result += 8

k = int(input())

for i in range(k):
  a, b = map(int, input().split())
  cog_rotate(a, b)

cog_check(first_deq, second_deq, third_deq, forth_deq)
print(result)