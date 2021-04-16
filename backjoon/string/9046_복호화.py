t = int(input())

for _ in range(t):
    cipher = list(input())
    cipher_dict = {}
    for word in cipher:
        if word != " ":
            try:
                cipher_dict[word] += 1
            except:    
                cipher_dict[word] = 1
    result = sorted(cipher_dict.items(), key=(lambda x:x[1]), reverse=True)
    if len(result) > 1:
        if result[0][1] == result[1][1]:
            print("?")
        else:
            print(result[0][0])
    else:
        print(result[0][0])
