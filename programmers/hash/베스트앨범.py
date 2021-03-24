def solution(genres, plays):
    answer = []
    dict = {}
    arr_order = {}
    for item in genres:
        dict[item] = []
    for i in range(len(plays)):
        dict[genres[i]].append({
            "plays":plays[i], 
            "index":i})
    for k, v in dict.items():
        sorted_v = sorted(v, key=(lambda x: (x['plays'], -x['index'])), reverse=True)
        dict[k] = sorted_v
        for value in v:
            try:
                arr_order[k] += value['plays']
            except:
                arr_order[k] = value['plays']
    sorted_arr_order = sorted(arr_order.items(), key=(lambda x: x[1]), reverse=True)
    for item in sorted_arr_order:
        count = 0
        for value in dict[item[0]]:
            count += 1
            if count > 2:
                break;
            else:
                answer.append(value['index'])
    return answer