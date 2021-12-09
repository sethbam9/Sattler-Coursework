
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

    def extract_min(self, pq):
        d = []
        for i in range(len(pq)):
            d.append(pq[i][0])
        m = min(d)
        i = d.index(m)
        pq.remove(pq[i])
        return m

    def dijkstra(self, node):
        # Initialize data structures
        inf = 100
        pred = [0] * len(self.matrix)
        dist = [0] * len(self.matrix)
        pq = []
        # Fill data structures
        for v in range(len(self.matrix)):
            pred[v] = -1
            if v != node:
                dist[v] = inf
            else:
                dist[v] = 0
            pq.append([v])
            pq[v].append(dist[v])
        # Compile the distances
        while (len(pq)) != 0:
            u = self.extract_min(pq)
            for v in range(len(self.matrix)):
                w = self.get_weight(u, v)
                if w != 0:
                    if dist[v] > (dist[u] + w):
                        dist[v] = (dist[u] + w)
                        pred[v] = u
                        if len(pq) >= v:
                            pq[v][1] = dist[v]
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

G.dijkstra(0)
