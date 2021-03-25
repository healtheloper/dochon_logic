import bisect

word = list(map(str, input().upper()))
INF = int(1e9)
word_dict = {}
for item in word:
    try:
        word_dict[item] += 1
    except:
        word_dict[item] = 1
sorted_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

if len(sorted_dict) > 1:
    if sorted_dict[0][1] == sorted_dict[1][1]:
        print("?")
    else:
        print(sorted_dict[0][0])
else:
    print(word[0])
