#Name - Win Yu Maung, Id - 6612054, Sec - 542

adj_pair = list(map(int,input().split()))
v = adj_pair[0]
e = adj_pair[1]

def createEdgeList(e):
    edgeList = []
    for i in range(e):
        mylist = list(map(int, input().split()))
        edgeList.append((mylist[0],mylist[1]))
    return edgeList

def matrix(v, edgeList):
    matrix = [[0] * v for r in range(v)]
    for i in range(v):
        for j in range(v):
            if (i, j) in edgeList or (j, i) in edgeList:
                matrix[i][j] = 1
                matrix[j][i] = 1
    return matrix

def display(v, matrix):
    v_list = []
    for i in range(v):
        v_list.append(i)

    print("   ", end="")
    for i in v_list:
        print(i, end="  ")

    print()
    for i in range(len(matrix)):
        print(v_list[i], end=" ")
        print(matrix[i])

edgeList = createEdgeList(e)
adj_matrix = matrix(v, edgeList)
display(v, adj_matrix)