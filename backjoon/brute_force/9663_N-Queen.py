n = int(input())
col = [0] * (16)
result = 0

def promising(i):
    for j in range(1, i):
        if col[i] == col[j] or abs(col[i]-col[j]) == i-j:
            return False;
    return True
def queens(i):
    if i==n:
        global result
        result += 1
    else:
        for j in range(1, n+1):
            col[i+1]=j
            if promising(i+1):
                queens(i+1)

queens(0)
print(result)