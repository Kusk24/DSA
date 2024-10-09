#Name - Win Yu Maung
#ID - 6612054
#Section - 542

import sys

from Week7.BinarySearchTree import BSTree

sys.setrecursionlimit(10001)

root = None        

class node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.p = None
        self.left = None
        self.right = None


def Inorder_Tree_Walk(x):
    if x != None:
        Inorder_Tree_Walk(x.left)
        print(x.key)
        Inorder_Tree_Walk(x.right)

def Tree_Minimum(x):
    # Replace "pass" with your code
    if x.left == None:
        return x
    else:
        return Tree_Minimum(x.left)

def Tree_Maximum(x):
    # Replace "pass" with your code
    if x.right == None:
        return x
    else:
        return Tree_Maximum(x.right)

def Tree_Successor(x):
    # Replace "pass" with your code
    x = Tree_Search(x)
    if x.right is not None:
        return Tree_Minimum(x.right)
    y = x.p
    while y is not None and x == y.right:
        x = y
        y = y.p
    return y

'''
Adding your own Tree_Predecessor(x) is recommended, but not required
'''
def Tree_Predecessor(x):
    x = Tree_Search(x)
    if x.left is not None:
        return Tree_Maximum(x.left)
    y = x.p
    while y is not None and x == y.left:
        x = y
        y = y.p
    return y
    

def Transplant(u, v):
    # This function is required for supporting Tree_Delete
    # Replace "pass" with your code
    if u.p is None:
        root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v is not None:
        v.p = u.p
     

def Tree_Delete(z):
    # Replace "pass" with your code
    z = Tree_Search(z)
    if z.left == None:
        Transplant(z,z.right)
    elif z.right == None:
        Transplant(z,z.left)
    else:
        y = Tree_Minimum(z.right)
        if y.p != z:
            Transplant(y,y.right)
            y.right = z.right
            y.right.p = y
        Transplant(z,y)
        y.left = z.left
        y.left.p = y
    return(z.key)

def Tree_Search(k):
    global root
    def Searching(root,k): #to return k if found
        if k == root.key:
            return root
        elif k < root.key:
            if root.left == None:
                return None
            else:
                return Searching(root.left, k)
        else:
            if root.right == None:
                return None
            else:
                return Searching(root.right, k)

    return Searching(root, k)
    # Replace "pass" with your code
    
def Tree_Insert(z):
    global root
    y = None
    x = root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    # Replace "pass" with your code
    

# Function to print
def printCall ( node , indent , last ) :
    if node != None :
        print(indent, end=' ')
        if last :
            print ("R----",end= ' ')
            indent += "     "
        else :
            print("L----",end=' ')
            indent += "|    "

        print ( str ( node.key ) )
        printCall ( node.left , indent , False )
        printCall ( node.right , indent , True )

# Function to call print
def print_BSTree (root) :
    printCall( root , "" , True )


# Tree_Insert(node(30, ""))
# Tree_Insert(node(5, ""))
# Tree_Insert(node(17, ""))
# Tree_Insert(node(23, ""))
# Tree_Insert(node(2, ""))
# Tree_Insert(node(76, ""))
# Tree_Insert(node(42, ""))
# Tree_Insert(node(57, ""))
# Tree_Insert(node(12, ""))
# Tree_Insert(node(25, ""))
# Tree_Insert(node(36, ""))
#
# print_BSTree(root)
#
# minimum = Tree_Minimum(root)
# print("The minimum key is: ", minimum.key)
# maximum = Tree_Maximum(root)
# print("The maximum key is: ", maximum.key)
#
# if Tree_Search(12):
#     print("There is ",Tree_Search(12).key," in the tree")
# else:
#     print("Not Found")
#
# successor = Tree_Successor(42)
# print("The successor is: ", successor.key)
#
# predecessor = Tree_Predecessor(42)
# print("The predecessor is: ", predecessor.key)
#
# print("Deleted,", Tree_Delete(12), "from the tree")
# print_BSTree(root)
#
# if Tree_Search(12):
#     print("There is ",Tree_Search(12).key," in the tree")
# else:
#     print("Not Found")

Tree_Insert(node(85, ""))
Tree_Insert(node(19, ""))
Tree_Insert(node(4, ""))
Tree_Insert(node(5, ""))
Tree_Insert(node(34, ""))
Tree_Insert(node(180, ""))
Tree_Insert(node(42, ""))
print_BSTree(root)

Tree_Delete(19)
print_BSTree(root)

Tree_Delete(85)
print_BSTree(root)
