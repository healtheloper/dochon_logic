import sys

input = sys.stdin.readline

count = int(input())
int_dict = {}
for _ in range(count):
    data = int(input())
    try:
        int_dict[data] += 1
    except:
        int_dict[data] = 1
sorted_dict = sorted(int_dict.items())

for item in sorted_dict:
    item_count = item[1]
    item_value = item[0]
    for _ in range(item_count):
        print(item_value)