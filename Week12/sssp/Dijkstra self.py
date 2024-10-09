#Name - Win Yu Maung, ID - 6612054, Sec - 542

from Heap import *

type = input()
V, E = map(int, input().split())
edgeList = []

for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertices(self, vertices):
        for vertex in vertices:
            self.vertices.append(vertex)

class Vertex:
    def __init__(self, value):
        self.value = value
        self.key = 0
        self.parent = None
        self.edges = []

    def add_edge(self, to_vertex, weight):
        self.edges.append(Edge(to_vertex, weight))


class Edge:
    def __init__(self, v, w):
        self.vertex = v
        self.weight = w


G = Graph()
vertices = []
for i in range(V):
    vertices.append(Vertex(i))

for i in range(len(edgeList)):
    u = edgeList[i][0]
    v = edgeList[i][1]
    w = edgeList[i][2]
    if type == "Undirected Graph":
        vertices[u-1].add_edge(v, w)
        vertices[v-1].add_edge(u, w)
    else:
        vertices[u-1].add_edge(v, w)

G.add_vertices(vertices)

def myCompare(x,y):
    return x.weight < y.weight

def Dijkstra(G,s):
    S = [False] * len(G.vertices)
    Shortest_Estimate = ['inf'] * len(G.vertices)


    a = Vertex(s)
    a.key = 0
    a.parent = None

    Q = [a]

    while len(Q) >= 1:
        PQ = heap(items = Q[0].edges , cmp = myCompare)
        t = PQ.extract()
        u = t.vertex
        if not S[u]:
            S[u] = True
            for v in G.vertices[u].edges:
                if S[v.vertex] == False and Shortest_Estimate[u] + v.weight < Shortest_Estimate[v.vertex]:
                    a.vertex = v.vertex
                    a.key = Shortest_Estimate[v.vertex] = Shortest_Estimate[u] + v.weight
                    a.parent = u
                    Q[0] = a
        if u == V - 1:
            return Shortest_Estimate

print(Dijkstra(G, 2))