
# Graph from Figure 2.28 (pg. 55):
     # 0,1,2,3,4,5,6,7,8
G =  [[0,1,1,1,0,0,0,0,0],#0
      [1,0,0,0,1,0,0,0,0],#1
      [1,0,0,0,0,0,0,0,0],#2
      [1,0,0,0,0,1,0,0,0],#3
      [0,1,0,0,0,1,0,0,0],#4
      [0,0,0,1,1,0,0,1,1],#5
      [0,0,0,0,0,0,0,0,0],#6
      [0,0,0,0,0,1,0,0,0],#7
      [0,0,0,0,0,1,0,0,0]]#8

# Create 'visited' & 'inqueue' lists with 8 * 8 False values
dfs_visited = []
bfs_visited = []
dfs_edges = []
bfs_edges = []
inqueue = []
Q = []

# Fill the lists for DFS and BFS with False
for i in range(9):
    dfs_visited.append(False)
    bfs_visited.append(False)
    inqueue.append(False)

# Depth-First-Search Algorithm - - - - - - - - - - - - - - - - - - - - - - - -
def DFS(n):
    dfs_visited[n] = True
    for v in range(9):
        if G[n][v] == 1 and not dfs_visited[v]:
            dfs_visited[v] = True
            edge = "%s--%s" % (n, v)
            dfs_edges.append(edge)
            DFS(v)

# Breadth-First-Search Algorithm: - - - - - - - - - - - - - - - - - - - - - -
def IsQueueEmpty(Q): #returns true if the queue Q is empty, false otherwise.
    if len(Q) == 0:
        return True
    else:
        return False

def Enqueue(i): #adds item i to the tail of the queue Q.
    Q.append(G[i])

def Dequeue(Q): #removes an item from the front (head) of the queue.
    Q.pop(0)

def BFS(n):
    for n in range(9):
        Enqueue(n)
        inqueue[n] = True
        while not IsQueueEmpty(Q):
            Dequeue(Q)
            inqueue[n] = False
            bfs_visited[n] = True
            for v in range(9):
                if not bfs_visited[v] and not inqueue[v]:
                    if G[n][v] == 1:
                        Enqueue(v)
                        inqueue[v] = True
                        edge = "%s--%s" % (n, v)
                        bfs_edges.append(edge)

DFS(0)
BFS(0)
print("DFS edges:", dfs_edges)
print("BFS edges:", bfs_edges)
