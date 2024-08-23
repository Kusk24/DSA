#part 1

def insert_reservation(R, t, k):
    for i in range(len(R)):
        if abs(R[i] - t) < k:
            print("Cannot be added , full reservation")
            return R  # The new reservation cannot be added

    # If valid, insert t while keeping the list sorted
    R.append(t)
    R.sort()
    print("Reservation added")
    return R

# Example usage
R = [17, 21, 26, 29, 36]
t = 24
k = 3
print(insert_reservation(R, t, k))# Output should be [17, 21, 24, 26, 29, 36]
time = int(input("Enter reserve time: "))
print(insert_reservation(R, time, k))

#part 2
"""
For insertion into a sorted list and maintaining the order, the upper bound on the running time is 
𝑂
(
𝑛
)
O(n), where 
𝑛
n is the number of reservations in the list. This is because in the worst case, you might have to shift all elements to insert the new element at the correct position.

"""

#part 3

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_bst(root, t, k):
    if root is None:
        return TreeNode(t)
    if abs(root.val - t) < k:
        return root  # The new reservation cannot be added
    if t < root.val:
        root.left = insert_bst(root.left, t, k)
    else:
        root.right = insert_bst(root.right, t, k)
    return root

# Helper function to perform inorder traversal to get a sorted list
def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)

# Example usage
reservations = [17, 21, 26, 29, 36]
root = None
for r in reservations:
    root = insert_bst(root, r, k)

t = 24
root = insert_bst(root, t, k)
sorted_reservations = []
inorder(root, sorted_reservations)
print(sorted_reservations)  # Output should be [17, 21, 24, 26, 29, 36]

#part 4
"""
Part d: Running Time in BST
For the BST, the insertion time in the worst case (unbalanced tree) is 
𝑂
(
𝑛
)
O(n). However, if the BST is balanced (like an AVL tree or Red-Black tree), the running time is 
𝑂
(
log
⁡
𝑛
)
O(logn). Checking the constraints for each insertion would add a constant time operation, so the overall complexity remains 
𝑂
(
log
⁡
𝑛
)
O(logn) for balanced trees.
"""
