def solution(phone_book):
    dict = {}
    count = 0
    for item in phone_book:
        dict[item] = True
    for item in phone_book:
        length = len(item)
        for i in range(len(item)):
            value = item[0:length]
            try:
                if dict[value]:
                    count += 1  
                    length -= 1
            except KeyError:
                length -= 1
                continue
    if count > len(phone_book):
        return False
    else:
        return True