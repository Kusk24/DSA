#Name - Win Yu Maung, Id- 6612054, Sec -542

from topological_sort import *

adj_pair = list(map(int,input().split()))
v = adj_pair[0]
e = adj_pair[1]

mydict = {}
for i in range(v):
    mydict[i] = []

for i in range(e):
    mylist = list(map(int, input().split()))
    mydict[mylist[0]].append(mylist[1])

print("Topological sorted vertices: ", topological_sort(v, mydict))


