#Name - Win Yu Maung, ID - 6612054, Sec - 542

from Heap import *

V,E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

class Graph:
    def __init__(self, v, e, edgeList):
        self.V = v
        self.E = e
        self.Adj = edgeList

class Vertex:
    def __init__(self, index):
        self.index = index
        self.key = float('inf')
        self.parent = None

def tuple(e):
    return e[2]

# def MST_PRIM(G,r):
#     A = 0
#     for u in G.V:
#         u.key = float('inf')
#         u.p = None
#     r.key = 0
#     Q = heap(items=G.V)
#     while Q != 0:
#         u = Q.extract()
#         A += u
#         for v in G.Adj[u]:
#             if v in Q and tuple(v) < v.key:
#                 v.p = u
#                 v.key = tuple(v)
#
#     return A
# G = Graph(V,E,edgeList)
# MST_PRIM(G,G.V)


G = Graph(V,E,edgeList)


def MST_PRIM(G):
    for u in G.V:
        MST = [""] * G.V
        MinKey = ['inf'] * G.V
    s.vertex = 0
    s.key = 0


 # start.in_tree = True
    # Q = [heap(items = start.edges, cmp = mycompare)]
    # # print(Q[0])
    #
    # while not len(Q) == 0:
    #     smallest = Q[0].extract()
    #     next_vertex = graph.vertices[smallest.vertex]
    #
    #     if next_vertex.in_tree:
    #         continue
    #     else:
    #         next_vertex.in_true = True
    #         mst_edges.append((start.value, smallest.vertex, smallest.weight))
    #         mst_weight += smallest.weight
    #         Q[0] = heap(items = next_vertex.edges, cmp = mycompare)