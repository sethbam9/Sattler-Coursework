
class Graph:
    def __init__(self, v, e):
        self.v = v
        self.e = e
        self.matrix = [[0 for i in range(v)]
                          for j in range(v)]

    def get_weight(self, frm, to):
        return self.matrix[frm][to]

    def add_edge(self, frm, to, weight):
        self.matrix[frm][to] = weight
        self.matrix[to][frm] = weight

    def b_ford(self, node):
        # Initialize data structures
        inf = 100
        q = []
        in_q = []
        dist = []
        pred = []
        # Fill data structures
        for v in range(len(self.matrix)):
            pred.append(-1)
            if v != node:
                dist.append(inf)
                in_q.append(False)
            else:
                dist.append(0)
                in_q.append(True)
        q.append(node)
        # Compile the distances
        while (len(q)) != 0:
            u = q.pop()
            in_q[u] = False
            for v in range(len(self.matrix)):
                w = self.get_weight(u, v)
                if w != 0:
                    if dist[v] > (dist[u] + w):
                        dist[v] = (dist[u] + w)
                        pred[v] = u
                        if not in_q[v]:
                            q.append(v)
                            in_q[v] = True
            print(dist)
        print("pred: ", pred)
        print("dist: ", dist)

# Create graph object
G = Graph(16, 24)

G.add_edge(0, 1, 3)
G.add_edge(1, 2, 1)
G.add_edge(2, 3, 4)
G.add_edge(0, 4, 5)
G.add_edge(1, 5, 9)
G.add_edge(2, 6, 2)
G.add_edge(3, 7, 6)
G.add_edge(4, 5, 3)
G.add_edge(5, 6, 5)
G.add_edge(6, 7, 8)
G.add_edge(4, 8, 7)
G.add_edge(5, 9, 9)
G.add_edge(6, 10, 3)
G.add_edge(7, 11, 2)
G.add_edge(8, 9, 8)
G.add_edge(9, 10, 4)
G.add_edge(10, 11, 6)
G.add_edge(8, 12, 6)
G.add_edge(9, 13, 4)
G.add_edge(10, 14, 3)
G.add_edge(11, 15, 3)
G.add_edge(12, 13, 3)
G.add_edge(13, 14, 2)
G.add_edge(14, 15, 7)

G.b_ford(0)
