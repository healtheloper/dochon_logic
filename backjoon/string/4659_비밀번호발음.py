while True:
    data = input()
    if data == "end":
        break
    vowel = ["a","e","i","o","u"]
    cur_char = ''
    cur_count = 0
    conso_count = 0
    vo_count = 0
    vo_count_all = 0
    isAccept = True
    for char in data:
        if char not in vowel:
            conso_count += 1
            vo_count = 0
        elif char in vowel:
            vo_count += 1
            vo_count_all += 1
            conso_count = 0
        if char == cur_char and (cur_char != "o" and cur_char != "e"):
            if cur_char == "e" or cur_char == "o":
                if cur_count < 2:
                    continue
                else:
                    isAccept = False
                    break
            else:
                isAccept = False
                break

        if conso_count == 3 or vo_count == 3:
            isAccept = False
            break

        cur_char = char

    if isAccept and vo_count_all != 0:
        print(f"<{data}> is acceptable")
    else:
        print(f"<{data}> is not acceptable")