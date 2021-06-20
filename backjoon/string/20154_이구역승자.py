alp = {
"A":3,"B":2,"C":1,"D":2,"E":3,"F":3,"G":3,"H":3,"I":1,"J":1,"K":3,"L":1,"M":3,"N":3,"O":1,"P":2,"Q":2,"R":2,"S":1,"T":2,"U":1,"V":1,"W":2,"X":2,"Y":2,"Z":1}

data = input()
result = 0
def tot(arr):
    if len(arr) == 1:
        global result
        result = arr[0] % 10
        return
    temp=0
    temp_arr=[]
    for i in range(len(arr)):
        if i % 2 == 0:
            temp += arr[i]
            if i == len(arr)-1:
                temp_arr.append(temp)
        else:
            temp += arr[i]
            temp_arr.append(temp)
            temp = 0
    tot(temp_arr)

q = []
for i in list(data):
    q.append(alp[i])
tot(q)
if result % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")
        