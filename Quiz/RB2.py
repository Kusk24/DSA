class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = "Red"  # New nodes are red by default

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = "Black"  # TNULL is always black (represents NULL)
        self.root = self.TNULL

    # Preorder traversal with color printing
    def pre_order_helper(self, node):
        if node != self.TNULL:
            print(f'{node.data}({node.color})', end=" ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    # Inorder traversal with color printing
    def in_order_helper(self, node):
        if node != self.TNULL:
            self.in_order_helper(node.left)
            print(f'{node.data}({node.color})', end=" ")
            self.in_order_helper(node.right)

    # Postorder traversal with color printing
    def post_order_helper(self, node):
        if node != self.TNULL:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            print(f'{node.data}({node.color})', end=" ")

    # Search the tree for a key
    def search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.data:
            return node

        if key < node.data:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    # Fix the Red-Black Tree after deletion
    def fix_delete(self, x):
        while x != self.root and x.color == "Black":
            if x == x.parent.left:
                s = x.parent.right
                if s.color == "Red":
                    s.color = "Black"
                    x.parent.color = "Red"
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == "Black" and s.right.color == "Black":
                    s.color = "Red"
                    x = x.parent
                else:
                    if s.right.color == "Black":
                        s.left.color = "Black"
                        s.color = "Red"
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = "Black"
                    s.right.color = "Black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == "Red":
                    s.color = "Black"
                    x.parent.color = "Red"
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.left.color == "Black" and s.right.color == "Black":
                    s.color = "Red"
                    x = x.parent
                else:
                    if s.left.color == "Black":
                        s.right.color = "Black"
                        s.color = "Red"
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = "Black"
                    s.left.color = "Black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "Black"

    # Fix the Red-Black Tree after insertion
    def fix_insert(self, k):
        while k.parent.color == "Red":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "Red":
                    u.color = "Black"
                    k.parent.color = "Black"
                    k.parent.parent.color = "Red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "Black"
                    k.parent.parent.color = "Red"
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "Red":
                    u.color = "Black"
                    k.parent.color = "Black"
                    k.parent.parent.color = "Red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "Black"
                    k.parent.parent.color = "Red"
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "Black"

    # Left rotate
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Right rotate
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Insert a new node
    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = "Red"  # New node is always red

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = "Black"
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    # Delete a node from the tree
    def delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.data == key:
                z = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Key not found in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == "Black":
            self.fix_delete(x)

    # Replace the nodes
    def rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    # Pre-order traversal
    def preorder(self):
        self.pre_order_helper(self.root)
        print()

    # In-order traversal
    def inorder(self):
        self.in_order_helper(self.root)
        print()

    # Post-order traversal
    def postorder(self):
        self.post_order_helper(self.root)
        print()

    # Print tree structure
    def print_tree(self, node, level=0, prefix="Root: "):
        if node != self.TNULL:
            print(" " * (level * 4) + prefix + f'{node.data}({node.color})')
            self.print_tree(node.left, level + 1, "L--- ")
            self.print_tree(node.right, level + 1, "R--- ")

# Main program for user input
if __name__ == "__main__":
    rbt = RedBlackTree()
    while True:
        print("\n1. Insert a node")
        print("2. Delete a node")
        print("3. In-order traversal")
        print("4. Pre-order traversal")
        print("5. Post-order traversal")
        print("6. Print tree structure")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            key = int(input("Enter the value to insert: "))
            rbt.insert(key)
        elif choice == 2:
            key = int(input("Enter the value to delete: "))
            rbt.delete_node_helper(rbt.root, key)
        elif choice == 3:
            print("In-order traversal:")
            rbt.inorder()
        elif choice == 4:
            print("Pre-order traversal:")
            rbt.preorder()
        elif choice == 5:
            print("Post-order traversal:")
            rbt.postorder()
        elif choice == 6:
            print("Tree structure:")
            rbt.print_tree(rbt.root)
        elif choice == 7:
            break
        else:
            print("Invalid choice! Please enter again.")
            

