#Name - Win Yu Maung, ID - 6612054, Sec -542
mystring = input()
graph_type = input()
V,E = map(int, input().split())
adj_list = [[] for v in range(V)]
for i in range(E):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    if v not in adj_list[u]:
        adj_list[u].append(v)

    # For undirected graph, also add the reverse edge (v -> u)
    if graph_type == 'Undirected Graph':
        if u not in adj_list[v]:
            adj_list[v].append(u)
    # adj_list[u].append(v)
    # if graph_type == 'Undirected Graph':
    #     adj_list[v].append(u)

color = ["WHITE"]*V
d = [-1]*V
p = [None]*V

# Write your Breast-First Search code below
color[0] = "GRAY"
d[0] = 0
Q = [0]

while len(Q) != 0:
    u = Q[0]
    for v in adj_list[u]:
        if color[v] == "WHITE":
            color[v] = "GRAY"
            d[v] = d[u] + 1
            p[v] = u
            Q.append(v)
    del Q[0]
    color[u] = "BLACK"
# print(color, adj_list)

# List = ["A","B","C","D","E","F","G","H","I","J","K","L","M","Z"]
Mydict = {}
for v in range(V):
    if d[v] == -1:
        dv = "Inf"
    else:
        dv = d[v]
    if p[v] != None:
        pv = p[v]+1
    else:
        pv = "None"

    # print("%d %5s" % (v+1, color[v]), dv, pv)
    # print(List[v], "=", dv )

    #for parent
    if pv == "None":
        print("parent of", mystring[v], "=", pv)
    else:
        print("parent of", mystring[v], "=", mystring[int(pv)-1])

    if dv in Mydict:
        Mydict[dv].append(mystring[v])
    else:
        Mydict[dv] = [mystring[v]]

for key,value in Mydict.items():
    print(value)