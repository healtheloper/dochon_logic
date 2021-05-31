square = {}

for _ in range(3):
    x, y = map(int, input().split())
    try:
        square[f"{x}x"] += 1
    except:
        square[f"{x}x"] = 1
    try:
        square[f"{y}y"] += 1
    except:
        square[f"{y}y"] = 1

square = sorted(square.items(), key=lambda x:x[1])
a, b = square[0][0], square[1][0]
if "x" in a:
    x1 = a.rstrip("x")
    y1 = b.rstrip("y")
else:
    x1 = b.rstrip("x")
    y1 = a.rstrip("y")
print(x1, y1)
