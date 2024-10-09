#Name - Win Yu Maung, ID - 6612054, Sec - 542

from Heap import *

class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.in_tree = False
        self.parent = None

    def add_edge(self, to_vertex, weight):
        self.edges.append(Edge(to_vertex, weight))


class Edge:
    def __init__(self, to_vertex, weight):
        self.vertex = to_vertex
        self.weight = weight


class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertices(self, vertices):
        for vertex in vertices:
            self.vertices.append(vertex)


def mycompare(x, y):
    return x.weight < y.weight


def MST_Prim(graph, start):
    mst_weight = 0
    mst_edges = []

    Q = heap(cmp=mycompare)
    start.in_tree = True

    for edge in start.edges:
        Q.insert(edge)

    while not Q.empty():
        smallest_edge = Q.extract()
        next_Vertex = graph.vertices[smallest_edge.vertex]

        if next_Vertex.in_tree:
            continue
        else:
            next_Vertex.in_tree = True
            mst_edges.append(smallest_edge)
            mst_weight += smallest_edge.weight

            for edge in next_Vertex.edges:
                if not graph.vertices[edge.vertex].in_tree:
                    Q.insert(edge)

    return mst_weight, mst_edges


V, E = map(int, input().split())
edgeList = []

for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

G = Graph()
vertices = []

for i in range(V):
    vertices.append(Vertex(i))

for i in range(len(edgeList)):
    u = edgeList[i][0]
    v = edgeList[i][1]
    w = edgeList[i][2]
    vertices[u].add_edge(v, w)
    vertices[v].add_edge(u, w)

G.add_vertices(vertices)

# for i in G.vertices:
#     print(i.value)
#     for e in i.edges:
#         print("Vertex", e.vertex)
#         print("Weight", e.weight)

mst_weight, mst_edges = MST_Prim(G, G.vertices[0])

print("Total MST weight is =", mst_weight)
# print(G.vertices[0].value, end = " ")
# for i in mst_edges:
#     print( i.vertex, end = " ")
