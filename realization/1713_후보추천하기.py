# 사진 틀의 개수, 1이상 20이하
n = int(input())
# 전체 학생의 총 추천 횟수, 1000번 이하
m = int(input())
# 추천받은 학생을 나타내는 번호, 1부터 100
datas = input().split()

photo_dic = {}

for item in datas:
  item = int(item)
  #dic이 차있지 않은 상태
  if(len(photo_dic) < n):
    try:
      photo_dic[item] += 1
    except KeyError:
      photo_dic[item] = 1
  #dic이 꽉 찼다면
  elif(len(photo_dic) >= n):
    try:
      photo_dic[item] += 1
    except KeyError:
      min_val = 1000
      idx = 0
      for key, val in photo_dic.items():
        if(val < min_val):
          min_val = val
          idx = key
      del photo_dic[idx]
      photo_dic[item] = 1

result = sorted(photo_dic.items())

# 출력
for idx, item in enumerate(result):
  if(idx+1 == len(result)):
    print(item[0])
  else:
    print(item[0], end=" ")