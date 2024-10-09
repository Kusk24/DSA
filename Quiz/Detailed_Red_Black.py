# Define Node
class RB_Node():
    def __init__(self, key, data=None):
        self.data = data
        self.key = key  # Key of Node
        self.p = None  # Parent of Node
        self.left = None  # Left Child of Node
        self.right = None  # Right Child of Node
        self.color = 1  # Red Node as new node is always inserted as Red Node

# Define R-B Tree
class RBTree():
    def __init__(self):
        self.NULL = RB_Node(0)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

    # Insert New Key
    def insert(self, key, rbt):
        print(f"Inserting {key}")
        node = RB_Node(key)
        node.p = None
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1  # New node is red
        self.RB_Insert(node, rbt)

    # Insert New Node
    def RB_Insert(self, node, rbt):
        print(f"RB_Insert: Adding node with key {node.key}")
        y = None
        x = self.root

        while x != self.NULL:  # Find position for new node
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.p = y  # Set parent of node as y
        if y == None:  # If parent is none, it becomes root
            print(f"{node.key} becomes the root node")
            self.root = node
        elif node.key < y.key:  # Check if it's a left or right child
            print(f"{node.key} is left child of {y.key}")
            y.left = node
        else:
            print(f"{node.key} is right child of {y.key}")
            y.right = node

        print("\nBefore fixing colors after insertion")
        rbt.print_RBTree()

        # Fix Red-Black Tree properties if violated
        if node.p == None:  # Root node is always black
            node.color = 0
            return

        if node.p.p == None:  # If the parent is root, no need to fix
            return

        self.fixInsert(node)  # Else fix the tree

    # Fixing up insertion
    def fixInsert(self, k):
        print(f"******Fixing tree after inserting {k.key}******")
        while k.p.color == 1:  # While parent is red
            if k.p == k.p.p.right:  # If parent is right child
                u = k.p.p.left  # Uncle is left child of grandparent
                if u.color == 1:  # If uncle is red
                    print(f"******Case 1: Recoloring node {k.key}'s parent {k.p.key} and uncle {u.key}******")
                    u.color = 0  # Set uncle black
                    k.p.color = 0  # Set parent black
                    k.p.p.color = 1  # Set grandparent red
                    k = k.p.p  # Move k up to grandparent
                else:
                    if k == k.p.left:  # If k is left child
                        print(f"******Case 2: Right rotation needed at {k.p.key}******")
                        k = k.p
                        self.RR(k)  # Right rotate
                    print(f"******Case 3: Left rotation needed at {k.p.p.key}******")
                    k.p.color = 0
                    k.p.p.color = 1
                    self.LR(k.p.p)
            else:  # Parent is left child
                u = k.p.p.right  # Uncle is right child of grandparent
                if u.color == 1:  # If uncle is red
                    print(f"******Case 1: Recoloring node {k.key}'s parent {k.p.key} and uncle {u.key}******")
                    u.color = 0
                    k.p.color = 0
                    k.p.p.color = 1
                    k = k.p.p
                else:
                    if k == k.p.right:  # If k is right child
                        print(f"******Case 2: Left rotation needed at {k.p.key}******")
                        k = k.p
                        self.LR(k)  # Left rotate
                    print(f"******Case 3: Right rotation needed at {k.p.p.key}******")
                    k.p.color = 0
                    k.p.p.color = 1
                    self.RR(k.p.p)
            if k == self.root:
                break
        self.root.color = 0  # Root is always black

    # Left rotate
    def LR(self, x):
        print(f"******Performing left rotation on {x.key}******")
        y = x.right  # Right child of x
        x.right = y.left  # Change right child of x to left child of y
        if y.left != self.NULL:
            y.left.p = x
        y.p = x.p  # Change parent of y to parent of x
        if x.p == None:  # If x is root
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    # Right rotate
    def RR(self, x):
        print(f"******Performing right rotation on {x.key}******")
        y = x.left  # Left child of x
        x.left = y.right  # Change left child of x to right child of y
        if y.right != self.NULL:
            y.right.p = x
        y.p = x.p  # Change parent of y to parent of x
        if x.p == None:  # If x is root
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    # Function to print
    def __printCall(self, node, indent, last):
        if node != self.NULL:
            print(indent, end=' ')
            if last:
                print("R----", end=' ')
                indent += "     "
            else:
                print("L----", end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.key) + "(" + s_color + ")")
            self.__printCall(node.left, indent, False)
            self.__printCall(node.right, indent, True)

    # Function to call print
    def print_RBTree(self):
        self.__printCall(self.root, "", True)

    # Deletion and Fixing (simplified steps added as well)
    def delete_node_helper(self, node, key, rbt):
        print(f"\nSearching for the node with key {key} to delete...")
        z = self.NULL
        while node != self.NULL:
            if node.key == key:
                z = node
            if node.key <= key:
                node = node.right
            else:
                node = node.left

        if z == self.NULL:
            print(f"Node with key {key} not found, deletion not possible.")
            return
        else:
            print(f"Node with key {key} found, proceeding with deletion.")
            print("Before Deletion:")
            rbt.print_RBTree()
            self.RB_Delete(z, rbt)

    def RB_Delete(self, z, rbt):
        print(f"Deleting node with key {z.key}")
        y = z
        y_original_color = y.color
        if z.left == self.NULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif z.right == self.NULL:
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.Tree_Minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color

        print("\nAfter Deletion, Before Fixing Colors")
        rbt.print_RBTree()

        if y_original_color == 0:
            print(f"Fixing up the tree after deletion of node {z.key}")
            self.fixDelete(x)

    def fixDelete(self, x):
        while x != self.root and x.color == 0:
            if x == x.p.left:
                s = x.p.right
                if s.color == 1:
                    print(f"*****Case 1: Sibling {s.key} is red. Performing left rotation and recoloring.*****")
                    s.color = 0
                    x.p.color = 1
                    self.LR(x.p)
                    s = x.p.right
                if s.left.color == 0 and s.right.color == 0:
                    print(f"*****Case 2: Both of sibling {s.key}'s children are black. Recoloring sibling.*****")
                    s.color = 1
                    x = x.p
                else:
                    if s.right.color == 0:
                        print(f"*****Case 3: Sibling {s.key}'s right child is black. Performing right rotation and recoloring.*****")
                        s.left.color = 0
                        s.color = 1
                        self.RR(s)
                        s = x.p.right
                    print(f"*****Case 4: Sibling {s.key}'s right child is red. Performing left rotation and recoloring.*****")
                    s.color = x.p.color
                    x.p.color = 0
                    s.right.color = 0
                    self.LR(x.p)
                    x = self.root
            else:
                s = x.p.left
                if s.color == 1:
                    print(f"*****Case 1: Sibling {s.key} is red. Performing right rotation and recoloring.*****")
                    s.color = 0
                    x.p.color = 1
                    self.RR(x.p)
                    s = x.p.left
                if s.left.color == 0 and s.right.color == 0:
                    print(f"*****Case 2: Both of sibling {s.key}'s children are black. Recoloring sibling.*****")
                    s.color = 1
                    x = x.p
                else:
                    if s.left.color == 0:
                        print(f"*****Case 3: Sibling {s.key}'s left child is black. Performing left rotation and recoloring.*****")
                        s.right.color = 0
                        s.color = 1
                        self.LR(s)
                        s = x.p.left
                    print(f"*****Case 4: Sibling {s.key}'s left child is red. Performing right rotation and recoloring.*****")
                    s.color = x.p.color
                    x.p.color = 0
                    s.left.color = 0
                    self.RR(x.p)
                    x = self.root
        x.color = 0
        print("Deletion fix-up complete. Tree is now balanced.")

    def Tree_Minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def __rb_transplant(self, u, v):
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

if __name__ == "__main__":
    rbt = RBTree()
    while True:
        print("\n1. Insert a node")
        print("2. Delete a node")
        print("3. Print tree structure")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter the value to insert: "))
            rbt.insert(key, rbt)
            print("After insertion and color fixing")
            print("Tree structure:")
            rbt.print_RBTree()
            print()
        elif choice == 2:
            key = int(input("Enter the value to delete: "))
            rbt.delete_node_helper(rbt.root, key, rbt)
            print("After deletion and color fixing")
            print("Tree structure:")
            rbt.print_RBTree()
            print()
        elif choice == 3:
            print("Tree structure:")
            rbt.print_RBTree()
        elif choice == 4:
            break
        else:
            print("Invalid choice! Please enter again.")
