#Name - Win Yu Maung, ID - 6612054, Sec -542

graph_type = input()
V,E = map(int, input().split())
adj_list = [[] for v in range(V)]
for i in range(E):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    adj_list[u].append(v)
    if graph_type == 'Undirected Graph':
        # print(graph_type)
        # print(len(graph_type))
        adj_list[v].append(u)

color = ["WHITE"]*V
d = [-1]*V
p = [None]*V

# print(color, adj_list)

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



# The code below is for printing output

for v in range(V):
    if d[v] == -1:
        dv = "Inf"
    else:
        dv = d[v]
    if p[v] != None:
        pv = p[v]+1
    else:
        pv = "None"

    print("%d %5s" % (v, color[v]), dv, pv)

    #for 3a
    # if pv == "None":
    #     print("%d %5s" % (v, color[v]), dv, pv)
    # else:
    #     print("%d %5s" % (v, color[v]), dv, pv-1)

    # for 3b
    # if pv == "None":
    #     print("v%d %5s" % (v+1, color[v]), dv, pv)
    # else:
    #     print("v%d %5s" % (v+1, color[v]), dv, f"v{pv}")

