
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

    def calc_strongest_paths(self):
        n = self.v
        W = self.matrix
        inf = -10
        S = [[0 for i in range(n)]
                for j in range(n)]
        pred = [[0 for i in range(n)]
                   for j in range(n)]

        for i in range(n):
            for j in range(n):
                if W[i][j] > W[j][i]:
                    S[i][j] = (W[i][j] - W[j][i])
                    pred[i][j] = i
                else:
                    S[i][j] = inf
                    pred[i][j] = -1

        for k in range(n):
            for i in range(n):
                if i != k:
                    for j in range(n):
                        if j != i:
                            if S[i][j] < min(S[i][k], S[k][j]):
                                S[i][j] = min(S[i][k], S[k][j])
                                pred[i][j] = pred[k][j]

        return print("Strongest Paths: %s \nPredecessors: %s" % (S, pred))

# Create graph object -- Page 236 (Figure 10.2)
G = Graph(5, 7)

G.add_edge(0, 2, 7)
G.add_edge(0, 4, 3)
G.add_edge(1, 0, 6)
G.add_edge(2, 4, 5)
G.add_edge(3, 1, 8)
G.add_edge(4, 1, 4)
G.add_edge(4, 3, 7)


G.calc_strongest_paths()
