
# Graph from Figure 6.7 (pg. 158):
G1 = {
    0: [[3,4], [1,10]],
    1: [[5,5], [2,7]],
    2: [[4,9], [3,0]],
    3: [[4,8]],
    4: [[5,1]],
    5: []
}
# Initialize lists
visited = []
sorted = []
pred = []
dist = []

for i in range(len(G1)):
    visited.append(False)
    sorted.append(False)
    pred.append(-1)
    dist.append(-1000)

# Ensure that the present node is larger than the previous.
def Sorted(n, v):
    global node
    global previous
    node = v
    previous = sorted[n]
    if node > previous:
        return True

def Sort(G, n):
    visited[n] = True
    sorted[n] = n
    for v in range(len(G)):
        if not visited[v] and Sorted(n, v):
            edge = "%s -> %s" % (n, v)
            print("Edge:", edge)
            Sort(G, v)

def CritPath(G):
    for u in sorted:
        for v in G[u]:
            if dist[v] < (dist[u] + G[0][0]):
                dist[v] = (dist[u] + G[0][0])
                pred[v] = u
    return (pred, dist)

if G[v] == []:
    
# CritPath(G1)
CritPath(G1)
print(sorted)
