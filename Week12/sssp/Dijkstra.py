#Name - Win Yu Maung, Id - 6612054, Sec - 542

from Heap_Decrease_Key import *

class Vertex:
    def __init__(self, value):
        self.value = value
        self.key = float('inf')
        self.parent = None
        self.edges = []

    def add_edge(self, to_vertex, weight):
        self.edges.append(Edge(to_vertex, weight))

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self, num_vertices):
        self.vertices = [Vertex(i) for i in range(num_vertices)]

    def add_edge(self, u, v, weight, is_undirected=False):
        self.vertices[u].add_edge(v, weight)
        if is_undirected:
            self.vertices[v].add_edge(u, weight)

def dijkstra(graph, source):
    graph.vertices[source].key = 0

    pq = heap(graph.vertices)

    while not pq.empty():
        u_index = pq.extract()
        u = graph.vertices[u_index]

        for edge in u.edges:
            v = graph.vertices[edge.vertex]
            new_dist = u.key + edge.weight

            if new_dist < v.key:
                v.key = new_dist
                v.parent = u
                pq.elevate_key(edge.vertex, new_dist)

    return graph.vertices

type_of_graph = input("")
V, E = map(int, input("").split())

G = Graph(V)
for _ in range(E):
    u, v, w = map(int, input().split())
    is_undirected = type_of_graph == "Undirected Graph"
    G.add_edge(u - 1, v - 1, w, is_undirected)

source_vertex = 0
vertices = dijkstra(G, source_vertex)

for v in range(len(vertices)):
    parent = vertices[v].parent.value + 1 if vertices[v].parent is not None else "None"
    print(f"{v + 1} {vertices[v].key} {parent}")