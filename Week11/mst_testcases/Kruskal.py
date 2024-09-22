#Name - Win Yu Maung, ID - 6612054, Sec - 542

from disjointsets3 import *

V,E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

class Graph:
    def __init__(self,V,edgeList):
        self.V = V
        self.E = edgeList

def tuple(e):
    return  (e[2])

def MST_Krukal(G):
    A = 0
    s = DisjointSets(V)
    G.E.sort(key = tuple, reverse = False)
    for i in G.E:
        if s.findset(i[0]) != s.findset(i[1]):
            A += tuple(i)
            s.union(s.findset(i[0]), s.findset(i[1]))
    return A

G = Graph(V,edgeList)
MST = MST_Krukal(G)
print(MST)