from itertools import permutations

k = int(input())
signs = input().split()
MAX = 9
MIN = 0

numbers = []
for i in range(10):
  numbers.append(i)

all_numbers = permutations(numbers, k+1)

result = []

def valid(item):
  for i in range(len(item)-1):
    if signs[i] == "<" and item[i] > item[i+1]:
      return False
    elif signs[i] == ">" and item[i] < item[i+1]:
      return False
  return True

for item in all_numbers:
  if valid(item):
    result.append(item)
  else:
    continue

for _ in result[len(result)-1]:
  print(_, end='')
print()
for _ in result[0]:
  print(_, end='')
print()