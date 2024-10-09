class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert a new node
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            queue = [self.root]
            while queue:
                temp = queue.pop(0)
                if not temp.left:
                    temp.left = new_node
                    new_node.parent = temp
                    break
                else:
                    queue.append(temp.left)
                if not temp.right:
                    temp.right = new_node
                    new_node.parent = temp
                    break
                else:
                    queue.append(temp.right)

    # Find the minimum node
    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Find the maximum node
    def find_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    # Find successor of a given node
    def find_successor(self, node):
        if node.right:
            return self.find_min(node.right)
        
        successor = node.parent
        while successor and node == successor.right:
            node = successor
            successor = successor.parent
        return successor

    # Find predecessor of a given node
    def find_predecessor(self, node):
        if node.left:
            return self.find_max(node.left)
        
        predecessor = node.parent
        while predecessor and node == predecessor.left:
            node = predecessor
            predecessor = predecessor.parent
        return predecessor

    # Delete a node from the tree
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root

    # Find a node by key
    def find_node(self, root, key):
        while root:
            if key < root.data:
                root = root.left
            elif key > root.data:
                root = root.right
            else:
                return root
        return None

    # In-order traversal
    def inorder(self):
        self.in_order_helper(self.root)
        print()

    def in_order_helper(self, node):
        if node:
            self.in_order_helper(node.left)
            print(f'{node.data}', end=" ")
            self.in_order_helper(node.right)

    # Pre-order traversal
    def preorder(self):
        self.pre_order_helper(self.root)
        print()

    def pre_order_helper(self, node):
        if node:
            print(f'{node.data}', end=" ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    # Post-order traversal
    def postorder(self):
        self.post_order_helper(self.root)
        print()

    def post_order_helper(self, node):
        if node:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            print(f'{node.data}', end=" ")

    # Print tree structure
    def print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.data))
            self.print_tree(node.left, level + 1, "L--- ")
            self.print_tree(node.right, level + 1, "R--- ")

# Main program for user input
if __name__ == "__main__":
    bt = BinaryTree()
    while True:
        print("\n1. Insert a node")
        print("2. Delete a node")
        print("3. In-order traversal")
        print("4. Pre-order traversal")
        print("5. Post-order traversal")
        print("6. Print tree structure")
        print("7. Find successor")
        print("8. Find predecessor")
        print("9. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            key = int(input("Enter the value to insert: "))
            bt.insert(key)
            bt.print_tree(bt.root)
        elif choice == 2:
            key = int(input("Enter the value to delete: "))
            bt.root = bt.delete(bt.root, key)
            print(f"Node with value {key} has been deleted.")
            bt.print_tree(bt.root)
        elif choice == 3:
            print("In-order traversal:")
            bt.inorder()
        elif choice == 4:
            print("Pre-order traversal:")
            bt.preorder()
        elif choice == 5:
            print("Post-order traversal:")
            bt.postorder()
        elif choice == 6:
            print("Tree structure:")
            bt.print_tree(bt.root)
        elif choice == 7:
            key = int(input("Enter the value to find successor: "))
            node = bt.find_node(bt.root, key)
            if node:
                successor = bt.find_successor(node)
                if successor:
                    print(f"Successor of {key} is {successor.data}")
                else:
                    print(f"No successor found for {key}")
            else:
                print(f"Node with value {key} not found.")
        elif choice == 8:
            key = int(input("Enter the value to find predecessor: "))
            node = bt.find_node(bt.root, key)
            if node:
                predecessor = bt.find_predecessor(node)
                if predecessor:
                    print(f"Predecessor of {key} is {predecessor.data}")
                else:
                    print(f"No predecessor found for {key}")
            else:
                print(f"Node with value {key} not found.")
        elif choice == 9:
            break
        else:
            print("Invalid choice! Please enter again.")
