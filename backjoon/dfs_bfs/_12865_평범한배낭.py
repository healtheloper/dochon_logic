import heapq
n, k = map(int, input().split())
max_profit = 0
w = []
p = []
for idx in range(n):
    a, b = map(int, input().split())
    w.append(a)
    p.append(b)
    

def bound(node):
    if node[1]["weight"] >= k:
        return
    else:
        result = node[0]
        j = node[1]["level"] + 1
        totWeight = node[1]["weight"]
        while j < n and totWeight+w[j] <= k:
            totWeight += w[j]
            result += p[j]
            j += 1
        x = j
        if x<n:
            result += (k-totWeight)*(p[x]/w[x])
        return result
node_v = [0, {
    "level":0,
    "weight":0,
    "bound":0
}]
node_u = [0, {
    "level":0,
    "weight":0,
    "bound":0
}]
node_w = [0, {
    "level":0,
    "weight":0,
    "bound":0
}]
node_v[1]["bound"] = bound(node_v)
q = []
heapq.heappush(q, node_v)
while q:
    profit, v = heapq.heappop(q)
    if v["bound"] > max_profit:
        node_u[1]["level"] = v["level"] + 1
        node_u[1]["weight"] = v["weight"] + w[node_u[1]["level"]]
        node_u[0] = profit + p[node_u[1]["level"]]
        if node_u[1]["weight"] <= k and node_u[0] > max_profit:
            max_profit = node_u[0]
        node_u[1]["bound"] = bound(node_u)
        if node_u[1]["bound"] > max_profit:
            heapq.heappush(q, node_u)
        
        node_w[1]["weight"] = node_v[1]["weight"]
        node_w[0] = profit
        node_w[1]["bound"] = bound(node_w)
        if node_w[1]["bound"] > max_profit:
            heapq.heappush(q, node_w)
print(max_profit)
