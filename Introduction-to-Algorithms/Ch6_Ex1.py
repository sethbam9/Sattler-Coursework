
# Unweighted Adj_Matrix from Table 6.1 / Figure 6.6 (pgs. 157-8):
      #0,1,2,3,4,5
G1 =  [[0,1,0,1,0,0],#0
      [0,0,1,0,0,1],#1
      [0,0,0,1,1,0],#2
      [0,0,0,0,1,0],#3
      [0,0,0,0,0,1],#4
      [0,0,0,0,0,0]]#5

# Graph from Figure 2.28 (pg. 55):
     # 0,1,2,3,4,5,6,7,8
G2 =  [[0,1,1,1,0,0,0,0,0],#0
      [1,0,0,0,1,0,0,0,0],#1
      [1,0,0,0,0,0,0,0,0],#2
      [1,0,0,0,0,1,0,0,0],#3
      [0,1,0,0,0,1,0,0,0],#4
      [0,0,0,1,1,0,0,1,1],#5
      [0,0,0,0,0,0,0,0,0],#6
      [0,0,0,0,0,1,0,0,0],#7
      [0,0,0,0,0,1,0,0,0]]#8

# Initialize lists
visited = []
sorted = []

for i in range(len(G2)):
    visited.append(False)
    # sorted.append(False)

# Ensure that the present node is larger than the previous.
def Sorted(n, v):
    global node
    global previous
    node = v
    # previous = sorted[n]
    if node > n:
        return True

# Depth-First-Search Topological Sort:
def Sort(G, n):
    visited[n] = True
    sorted.append(n)
    for v in range(len(G)):
        if G[n][v] == 1 and not visited[v] and Sorted(n, v):
            visited[v] = True
            edge = "%s -> %s" % (n, v)
            print("Edge:", edge)
            Sort(G, v)

# Input G1 for a directed graph or G2 for undirected:
Sort(G2, 0)
print("Sorted list:", sorted)
