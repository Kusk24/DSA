table_size = 10
table = [[] for i in range(table_size)]
print(table)
print(table[1])
table[1].append((1,2))
print(table[1])
print(any(1 in t for t in table[1]))

tab = [[('a',1)],[('b',2),('c',3),('d',4)],[('e',5),('f',6)]]
for i in tab:
    for j in i:
        print(j[0])
    print(i)

for i in range(len(tab)):
    print(tab[i][0][0])


'''
print(array, array2)
for key, value in array.items():
    if key, value in array2.items() and array[key] == array2[key] and a:
        count += 1
'''
