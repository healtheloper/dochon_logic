S = [1, 2, 3]
m = len(S)
N = 4
 
table = [[0 for x in range(m)] for x in range(N+1)]
for i in range(m):
    table[0][i] = 1
for i in range(1, N+1):
    for j in range(m):
        x = table[i - S[j]][j] if i-S[j] >= 0 else 0
        y = table[i][j-1] if j >= 1 else 0
        table[i][j] = x + y

print(table)
print(table[N][m-1])
 