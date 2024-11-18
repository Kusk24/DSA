import numpy as np

# a,b,c,d,e = range(1,6)
# print(a,b,c,d,e)

v1, v2, v3, v4, v5, v6 = range(6)
G1 = [[3, 1], [3, 2], [2, 3], [2, 1], [1, 3], [1, 2], [1, 0], [0, 1] ]
G2 = [["v1", "v2"]
    , ["v1", "v3"]
    , ["v3", "v2"]
    , ["v3", "v4"]
    , ["v4", "v3"]
      ]

G3 = [["v1", "v2"]
    , ["v1", "v3"]
    , ["v2", "v1"]
    , ["v2", "v3"]
    , ["v2", "v4"]
    , ["v2", "v5"]
    , ["v3", "v1"]
    , ["v3", "v2"]
    , ["v3", "v5"]
    , ["v4", "v2"]
    , ["v4", "v5"]
    , ["v4", "v6"]
    , ["v5", "v3"]
    , ["v5", "v2"]
    , ["v5", "v4"]
    , ["v5", "v6"]
    , ["v6", "v4"]
    , ["v6", "v5"]
      ]

A, B, D, F, N = range(5)
G4 = [["A", "B"]
    , ["B", "F"]
    , ["B", "D"]
    , ["F", "N"]
    , ["F", "A"]
    , ["N", "F"]
    , ["N", "B"]
    , ["D", "A"]
      ]

def AdjMatrixList(edgeList):
    vertexList = []
    for i in range(len(edgeList)):
        for j in range(2):
            vertexList.append(edgeList[i][j])#[A,B,B,F]
    #print(set(vertexList))
    vertexList = list(set(vertexList))
    vertexList.sort

    vertices = len(vertexList)

    adjMatrix = [[0 for i in range(vertices)] for j in range(vertices)]
    #print(adjMatrix)
    print(edgeList)
    for i,j in edgeList:
        x = vertexList.index(i)
        y = vertexList.index(j)
        adjMatrix[x][y] = 1
    
    adjList = []
    for i in range(len(vertexList)):
        temp = [vertexList[i]]
        for edge in edgeList:
            if edge[0] == vertexList[i]:
                temp.append(edge[1])
        adjList.append(temp)

    print("adjList:\n", adjList)
    print("adjMatrix:\n", np.array(adjMatrix), "\n")


AdjMatrixList(G1)
AdjMatrixList(G2)
AdjMatrixList(G3)
AdjMatrixList(G4)