#Name - Win Yu Maung, ID - 6612054, Sec - 542

V,E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

from disjointsets3 import DisjointSets

s = DisjointSets(V)

# Complete the code below

for i in (range(len(edgeList))):
     s.union(edgeList[i][0], edgeList[i][1])

connected = False

for i in range(V - 1):
    if s.findset(i) != s.findset(i + 1):
        connected = False
    else:
        connected = True

if connected:
    print("This graph is connected")
else:
    print("This graph is not connected")