#ID - 6612054
#Name - Win Yu Maung
#Sec - 542

plist = input("Enter a sequences of integers = ").split()
nlist = []
for i in plist:
    e = int(i)
    nlist.append(e)

print("\nFor Step 2")
print(nlist, end = " ")

print("\n \nFor Step 3")
for j in nlist:
    if j % 2 != 0:
        print(j, end = " ")

print("\n \nFor Step 4")
new = []
for j in nlist:
    if j%2 == 0:
        new.append(j)
        
new.sort()
if len(new) >= 1:
    print(new[-1], end = " ")

print("\n \nFor Step 5")
e = len(new) - 1
for i in new:
    print(new[e], end = " ")
    e -= 1
