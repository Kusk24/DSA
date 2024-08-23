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
print(new[-1])
