from collections import deque
import copy
bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
def truck_check(truck_count, q):
    truck_sums = 0
    p = copy.copy(q)
    if truck_count < len(truck_weights):
        for truck_dict in p:
            truck_sums += truck_dict["truck_weights"]
            if truck_sums+truck_weights[truck_count] < weight:
                q.append({"idx":truck_count, "truck_weights":truck_weights[truck_count]})
                truck_count += 1
def solution(bridge_length, weight, truck_weights):
    answer = 1
    dict = {}
    q = []
    q = deque()
    truck_count = 0
    q.append({"idx":0, "truck_weights":truck_weights[truck_count]})
    truck_count += 1
    while q:
        # 트럭 추가 확인
        truck_check(truck_count, q)
        # 트럭이 지나가는 것 +1
        print(q)
        answer += 1
        for truck_dict in copy.deepcopy(q):
            try:
                if dict[truck_dict["idx"]] < bridge_length-1:
                    dict[truck_dict["idx"]] += 1
                else:
                    q.popleft()
                    if len(q) == 0 and truck_count < len(truck_weights):
                        q.append({"idx":truck_count, "truck_weights":truck_weights[truck_count]})
                        truck_count += 1
                    else:
                        truck_check(truck_count, q)
            except:
                dict[truck_dict["idx"]] = 1
    return answer

print(solution(bridge_length, weight, truck_weights))