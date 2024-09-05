#Name - Win Yu Maung, Id - 6612054, Sec - 542

adj_pair = list(map(int,input().split()))
v = adj_pair[0]
e = adj_pair[1]

def buildEdgeDict(v):
    mydict = {}
    for i in range(v):
        mydict[i] = []
    return mydict

def addEdge(e, mydict):
    for i in range(e):
        mylist = list(map(int, input().split()))
        mydict[mylist[0]].append(mylist[1])
        mydict[mylist[1]].append(mylist[0])

def display(mydict):
    print("Adjacency_List")
    for key, value in mydict.items():
        print(key, "-->", value)

mydict = buildEdgeDict(v)
addEdge(e, mydict)
display(mydict)