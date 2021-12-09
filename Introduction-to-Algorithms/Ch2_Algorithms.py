# Algorithm 2.1: Recursive graph depth-ﬁrst search.
# DFS(G, node)
#   Input: G = (V, E), a graph
#       node, a node in G
#   Data: visited, an array of size |V|
#   Result: visited[i] is true if we have visited node i, false otherwise

visited[node] <- true
foreach v in AdjacencyList(G, node) do
    if not visited[v] then
        DFS(G, v)

# Algorithm 2.2: Factorial function.
# Factorial(n) → !n
#     Input: n, a natural number
#     Output: n!, the factorial of n

if n = 0 then
    return 1
else
    return n · Factorial(n − 1)

# Algorithm 2.3: Graph depth-ﬁrst search with a stack.
# StackDFS(G, node) → visited
#     Input: G = (V, E), a graph
#         node, the starting vertex in G
#     Output: visited, an array of size |V| such that visited[i] is true if we
#         have visited node i, false otherwise

S <- CreateStack()
visited <- CreateArray(|V|)
for i <- 0 to |V| do
    visited[i] <- false
Push(S, node)
while not IsStackEmpty(S) do
    c <- Pop(s)
    visited[c] <- true
    foreach v in AdjacencyList(G,c) do
        if not visited[v] then
            Push(S, v)
return visited

CreateQueue(), creates an empty queue.
Enqueue(Q, i ) adds item i to the tail of the queue Q.
Dequeue(Q) removes an item from the front of the queue. In essence, it removes the
head and makes the element following it the new head. If the queue is empty, then
the operation is not allowed (we get an error).
IsQueueEmpty(Q) returns true if the queue Q is empty, false otherwise.

# BFS(G, node) → visited
#     Input: G = (V, E), a graph
#         node, the starting vertex in G
#     Output: visited, an array of size |V| such that visited[i] is true if we
#         have visited node i, false otherwise

Q <- CreateQueue()
visited <- CreateArray(|V|)
inqueue <- CreateArray(|V|)
for i <- 0 to |V| do
    visited[i] <- false
    inqueue[i] <- false
Enqueue(Q, node)
inqueue[node] <- true
while not IsQueueEmpty(Q) do
    c <- Dequeue(Q)
    inqueue[c] <- false
    visited[c] <- true
    foreach v in AdjacencyList(G, c) do
        if not visited[v] and not inqueue[v] then
            Enqueue(Q, v)
            inqueue[v] <- true
return visited
