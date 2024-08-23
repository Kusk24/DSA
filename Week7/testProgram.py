# #Name - Win Yu Maung
# #ID - 6612054
# #Sec - 542
# # ---- BS Tree -----
from BinarySearchTree import *
import random
import time

#Step 2
bst = BSTree()
a = [20, 10, 77, 13, 27, 7, -3, 56, 26, 90, 97, 6, 33, 55, -2, 77]
# for i in range(16):
#     mylist.append(random.randint(a,b))
random.shuffle(a)

for k in a:
    x = BST_Node(k)
    bst.Tree_Insert(x)
    
bst.print_BSTree()

#Step 3
bst2 = BSTree()
a = 1
b = 10
mylist = [i for i in range(a,b+1)]

for k in mylist:
    x = BST_Node(k)
    bst2.Tree_Insert(x)

bst2.print_BSTree()
x = bst2.Tree_Search(9)
bst2.Tree_Delete(x)
bst2.print_BSTree()

#Step 4
counter = 0
n = 1000
k = 2*n
bst3 = BSTree()
for i in range(n):
    x = BST_Node(i)
    bst3.Tree_Insert(x)

st = time.process_time()
for i in range(n):
    v = random.randint(0,k)
    x = bst3.Tree_Search(v)
    if x != None:
        counter += 1
et = time.process_time()
print("Counter = " ,counter)
print("Running time by second = ",et-st)


# ---- RB Tree -----

from RedBlackTree import *
rbt = RBTree()
a = [12,5,3,11,15,7,10,13,14,6,4,17,8]
for k in a:
    rbt.insert(k)
rbt.print_RBTree()

rbt.delete(5)
rbt.print_RBTree()

#Step 7
rbt2 = RBTree()
a = 1
b = 10
mylist = [i for i in range(a,b+1)]
for k in mylist:
    x = RB_Node(k)
    rbt2.RB_Insert(x)

rbt2.print_RBTree()
x = rbt2.Tree_Search(9)
rbt2.RB_Delete(x)
rbt2.print_RBTree()

#Step8
n = 8000
counter = 0
k = 2*n # n is the number of keys inserted
rbt3 = RBTree()
for i in range(n):
    x = RB_Node(i)
    rbt3.RB_Insert(x)

st = time.process_time()
for i in range(n):
    v = random.randint(0, k)
    x = rbt3.Tree_Search(v) # rbt is the Red-Black Tree
    if x != rbt3.NULL:
        counter += 1
et = time.process_time()
print(counter)
print(et - st)

