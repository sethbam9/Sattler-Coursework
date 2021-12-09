# Graph implementation from https://www.bogotobogo.com/python/python_graph_data_structures.php

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def addEdge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

# if 2 > 1:

G = Graph()

G.add_vertex('a')
G.add_vertex('b')
G.add_vertex('c')
G.add_vertex('d')
G.add_vertex('e')
G.add_vertex('f')
G.add_vertex('g')
G.add_vertex('h')
G.add_vertex('i')
G.add_vertex('j')
G.add_vertex('k')
G.add_vertex('l')
G.add_vertex('m')
G.add_vertex('n')
G.add_vertex('o')
G.add_vertex('p')

G.addEdge('a', 'b', 3)
G.addEdge('b', 'c', 1)
G.addEdge('c', 'd', 4)
G.addEdge('a', 'e', 5)
G.addEdge('b', 'f', 9)
G.addEdge('c', 'g', 2)
G.addEdge('d', 'h', 6)
G.addEdge('e', 'f', 3)
G.addEdge('f', 'g', 5)
G.addEdge('g', 'h', 8)
G.addEdge('e', 'i', 7)
G.addEdge('f', 'j', 9)
G.addEdge('g', 'k', 3)
G.addEdge('h', 'l', 2)
G.addEdge('i', 'j', 8)
G.addEdge('j', 'k', 4)
G.addEdge('k', 'l', 6)
G.addEdge('i', 'm', 6)
G.addEdge('j', 'n', 4)
G.addEdge('k', 'o', 3)
G.addEdge('l', 'p', 3)
G.addEdge('m', 'n', 3)
G.addEdge('n', 'o', 2)
G.addEdge('o', 'p', 7)
print(G)
for v in G:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print ( vid, wid, v.get_weight(w))

for v in G:
    print (v.get_id(), G.vert_dict[v.get_id()])
Vertex(10).adjacent['a'] = 8
Vertex(10).adjacent['b'] = 4
Vertex('a').get_weight(0)

print(Vertex(6).get_id())
