from itertools import combinations

# N개의 줄 선언 (4<= N <= 20), N은 짝수
n = int(input())
half_n = int(n/2)
# 0으로 초기화된 NxN 이중배열 선언
arr = [[0 for _ in range(n)] for _ in range(n)]
# 조합을 위한 배열 선언
items = [0 for _ in range(n)]
for idx in range(n):
  items[idx] = idx+1
# 입력받은 값은 이중배열에 저장
for i in range(n):
  count = 0
  data = input().split()
  for item in data:
    arr[i][count] = int(item)
    count += 1

#만약 N이 4이면, 팀이 뽑아지는 경우의 수는
# 1,2 = 3,4 or 1,3 = 2,4 or 1,4 = 2,3
# 4C2 / 2 한 값과 같음
# 조합 순으로 보면 팀이 1=6, 2=5, 3=4 로 나누어 짐

comb = list(combinations(items, half_n))
comb_len = len(comb)
result = 1000
teams_count = [0 for _ in range(len(comb[0]))]

for item in range(len(comb[0])):
  teams_count[item] = item

for i in range(int(comb_len/2)):
  start = i
  link = len(comb)-i-1
  team_comb = list(combinations(teams_count, 2))
  start_team = 0
  link_team = 0
  for i in range(len(team_comb)):
    j = team_comb[i][0]
    k = team_comb[i][1]
    # 스타트팀 점수
    start_team += arr[comb[start][j]-1][comb [start][k]-1] + arr[comb[start][k]-1]  [comb[start][j]-1]
    # 링크팀 총 점수
    link_team += arr[comb[link][j]-1][comb [link][k]-1] + arr[comb[link][k]-1][comb [link][j]-1]
  # 차잇값 저장
  dif_team = abs(start_team - link_team)
  # 최솟값 저장
  if(result > dif_team):
    result = dif_team

print(result)