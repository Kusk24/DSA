mystring = input()
graph_type = input()
print(graph_type)
if graph_type != "Directed Graph":
    print("DFS only works on Directed Graph")
    exit()

V,E = map(int, input().split())
adj_list = [[] for v in range(V)]
for i in range(E):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    adj_list[u].append(v)

color = ["WHITE"]*V
p = [None]*V
time = 0
d = [-1]*V
f = [-1]*V

# Write your Depth-First Search code below
# Don't forget to make the initial dfs call! :)
def DFS_Visit(u):
    global time
    color[u] = "GRAY"
    d[u] = time
    time += 1
    for v in adj_list[u]:
        if color[v] == "WHITE":
            p[v] = u
            DFS_Visit(v)
    color[u] = "BLACK"
    f[u] = time
    time += 1

for u in range(V):
    if color[u] == "WHITE":
        DFS_Visit(u)

# print(color, adj_list)

# The code below is for printing output

for v in range(V):
    if d[v] == -1:
        dv = "undiscovered"
    else:
        dv = d[v]
    if f[v] == -1:
        fv = ""
    else:
        fv = f[v]
    if p[v] != None:
        pv = p[v]+1
    else:
        pv = "None"

    # print("%d %5s" % (v+1, color[v]), dv, fv, pv)
    if pv == "None":
        print(mystring[v], "= Discover -", dv, " & Finish -", fv, "       / Parent of", mystring[v] ,"is ", pv)
    else:
        print(mystring[v], "= Discover -", dv, " & Finish -", fv, "       / Parent of", mystring[v] ,"is", mystring[int(pv) - 1])

