def ternarySearch(low, high, find_value, values):
    while high >= low:
        # 첫 번째 구분 값
        mid1 = low + (high-low)//3
        # 두 번째 구분 값
        mid2 = low + 2*(high-low)//3

        # 값을 찾았다면 return
        if values[mid1] == find_value:
            return mid1
        if values[mid2] == find_value:
            return mid2
        
        # 첫 번째 영역에 있는지 탐색
        if find_value < values[mid1]:
            high = mid1-1
        # 세 번째 영역에 있는지 탐색
        elif find_value > values[mid2]:
            low = mid2+1
        # 두 번째 영역에 있는지 탐색
        elif values[mid1] < find_value and find_value < values[mid2]:
            low = mid1+1
            high = mid2-1
    # 만약 key 를 못찾았다면 -1 리턴
    return -1
    