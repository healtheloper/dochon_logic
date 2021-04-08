d = [[[0] * (51)] * (51)] * (51)

def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        d[a][b][c] = 1
        return 1
    if a>20 or b>20 or c>20:
        d[a][b][c] = w(20,20,20)
        return d[a][b][c]
    if a<b and b<c:
        if d[a][b][c] == 0:
            value = w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
            d[a][b][c] = value
            return value
        else:
            return d[a][b][c]
    else:
        if d[a][b][c] == 0:
            value = w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
            d[a][b][c] = value
            return value
        else:
            return d[a][b][c]
print(w(10,4,6))