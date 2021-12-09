
# Graph from Figure 2.10 (pg. 32):
              #A,B,C,D,E,F,G,H,I
Adj_Matrix = [[0,1,0,0,1,0,0,0,1],#A 0
              [1,0,0,0,0,0,0,1,0],#B 1
              [0,0,0,1,1,0,0,0,1],#C 2
              [0,0,1,0,0,0,0,0,0],#D 3
              [1,0,1,0,0,0,0,1,0],#E 4
              [0,0,0,0,0,0,1,0,1],#F 5
              [0,0,0,0,0,1,0,1,0],#G 6
              [0,1,0,0,1,0,1,0,0],#H 7
              [1,0,1,0,0,1,0,0,0]]#I 8

# Graph from Figure 2.28 (pg. 55):
       # 0,1,2,3,4,5,6,7,8
NBT =  [[0,1,1,1,0,0,0,0,0],#0
        [1,0,0,0,1,0,0,0,0],#1
        [1,0,0,0,0,0,0,0,0],#2
        [1,0,0,0,0,1,0,0,0],#3
        [0,1,0,0,0,1,0,0,0],#4
        [0,0,0,1,1,0,0,1,1],#5
        [0,0,0,0,0,0,0,0,0],#6
        [0,0,0,0,0,1,0,0,0],#7
        [0,0,0,0,0,1,0,0,0]]#8

G = Adj_Matrix
edges = []
colored = []
visited = []
color = "red"
next_color = "green"

for i in range(9):
    visited.append(False)
    colored.append(False)

# Add colored node to a list
def Bipartite(i):
    global color
    global next_color
    colored[i] = color
    temp = color
    color = next_color
    next_color = temp

# Depth-First-Search
def DFS(G, n):
    visited[n] = True
    if not colored[i]:
        colored[n] = color
    for v in range(9):
        if G[n][v] == 1 and not visited[v] and not colored[v]:
            visited[v] = True
            edge = "%s--%s" % (n, v)
            edges.append(edge)
            Bipartite(v)
            DFS(G, v)
        elif G[n][v] == 1 and colored[n] == colored[v]:
            print("This is not a bipartite graph")
            return
    return True

if DFS(G, 0):
    print("This is a bipartite graph")
if DFS(NBT, 0):
    print("This is a bipartite graph")
print(edges)
