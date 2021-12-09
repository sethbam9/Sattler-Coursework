
# I learned how to create a dictionary graph at:
# https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/

# Graph from Figure 6.4 (pg. 156)
G1 = {
    0: [1,2,3,4],
    1: [2],
    2: [],
    3: [4],
    4: [2,5],
}
# Initialize lists
visited = []
sorted = []
stack = []

for i in range(len(G1)):
    visited.append(False)
    sorted.append(False)

# Ensure that the present node is larger than the previous.
def Sorted(n, v):
    global node
    global previous
    node = v
    previous = sorted[n]
    if node > previous:
        return True

def Cycle(G, n):
    for i in G[n]:
        if i in stack:
            return print("C")

# Depth-First-Search Topological Sort:
def Sort(G, n):
    visited[n] = True
    stack.append(n)
    for v in range(len(G)):
        if not visited[v]:
            edge = "%s -> %s" % (n, v)
            print("Edge:", edge)
            Cycle(G, n)
            Sort(G, v)



Sort(G1, 0)
