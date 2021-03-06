#3 시험장의 개수 N
#3 4 5 각 시험장에 있는 응시자의 수 Ai
#2 2 B(총감독관) C(부감독관)

# 총 감독관은 1명, 부감독관은 여러명
# 응시자의 수 Ai 에서 B를 빼고 시작

n = int(input())
arr = input().split()
b, c = map(int, input().split())

# 초기 arr 설정 (총 감독관이 감독하는 수 뺀 초깃값)
for i, v in enumerate(arr):
  new_value = int(v) - b
  arr[i] = new_value

viewer_count = len(arr)

# 1, 2, 3
# 1  1  2
for idx, student_count in enumerate(arr):
  if student_count > 0:
    if int(student_count)%c == 0:
      count = int(int(student_count)/c)
    else:
      count = int(int(student_count) / c)+1
    viewer_count += count

print(viewer_count)