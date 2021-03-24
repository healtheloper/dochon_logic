from itertools import combinations

# def result(arr):
#     length = len(arr)
#     result = 0
#     for i in range(1, length+1):
#         comb = combinations(arr, i)
#         for j in comb:
#             temp = 1
#             for item in j:
#                 temp *= item
#             result += temp
#     return result

def result(arr):
    result = 1
    # (상의개수 + 안입는거(1))
    # * (하의개수 + 안입는거(1))
    # * ...
    # 총 개수에서 모두 안입는 경우의수 1개를 빼줌
    for item in arr:
        result *= (item+1)
    result -= 1
    return result

def solution(clothes):
    dict = {}
    kinds = []
    
    for item in clothes:
        dict[item[1]]=[]
        kinds.append(item[1])
    for item in clothes:
        dict[item[1]].append(item[0])
    kinds = set(kinds)
    kinds_count = []
    for i in kinds:
        kinds_count.append(len(dict[i]))
    answer = result(kinds_count)
    return answer