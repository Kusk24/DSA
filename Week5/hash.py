#Name - Win Yu Maung
#ID - 6612054
#Sec - 542

from sys import stdin


# Read the sequence of operations to be operated on the hash table
operations = []
for line in stdin:
    line = line.split()
    if len(line) > 2:
        line[2] = int(line[2])
    operations.append(line)


table_size = 10    # set table size here
hash_table = [[] for i in range(table_size)]

def show_hash_table():
    print('-------------------')
    for item_list in hash_table:
        print(item_list)
    print('-------------------')

def hash_func(s):
    sum = 0
    for i in s:
        c = ord(i)
        sum += c
    return sum % table_size
    # return the hash value
    

def insert(s, v):
    index = hash_func(s)
    if s not in dict(hash_table[index]):
        hash_table[index].append((s , v))
        return 0
    else:
        return -1
    
    # return 0 on successful insertion
    # return -1 if s has already been in the hash table

def search(s):
    index = hash_func(s)
    my_list = dict(hash_table[index])
    if s in my_list:
        return my_list[s]
    else:
        return -1
    return 0
    # return value of the key or
    # return -1 if s does not exists in hash table

def delete(s):
    index = hash_func(s)
    delete_index = 0
    if s not in dict(hash_table[index]):
        return -1
    else:
        for i in range(len(hash_table[index])):
            if hash_table[index][i][0] == s:
                delete_index = i
                break
        del hash_table[index][delete_index]
        return 0
    # return 0 on successful deletion
    # return -1 if s does not exists in hash table


# The main program to execute the sequence of operations
for op in operations:
    if op[0] == "insert":
        print(f"Inserting ({op[1]},{op[2]})")
        insert(op[1],op[2])
        show_hash_table()
    if op[0] == "search":
        print("Searching", op[1], "=" ,search(op[1]))
    if op[0] == "delete":
        print("Deleting" , op[1])
        delete(op[1])
        show_hash_table()

    # op[0] is "insert" or "search" or "delete"
print("\nFinal Hash Table")
show_hash_table()    

