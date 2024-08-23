#ID - 6612054
#Name - Win Yu Maung
#Sec - 541

plist = input("Enter a sequences of integers = ").split(" ")
nlist = []

for i in plist:
    e = int(i)
    nlist.append(e)

new = []
for j in nlist:
    if j%2 == 0:
        new.append(j)

new.sort()
e = len(new) - 1
for i in new:
    print(new[e])
    e -= 1
