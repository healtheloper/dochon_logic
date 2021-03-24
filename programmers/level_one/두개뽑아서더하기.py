# set 으로 답안을 제출하면 JSON 형태로 제출되어 배열로 재정의
# 문제 내에 오름차순으로 정렬 같은 말이 있는지 확인하기
def solution(numbers):
    answer = []
    result = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                value = numbers[i]+numbers[j]
                result.append(value)
    result = set(result)
    for i in result:
        answer.append(i)
    answer.sort()
    return answer