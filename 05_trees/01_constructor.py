# tree = {"value": 4,
#         "left": {"value": 3, "left": None, "right": None},
#         "right": {"value": 23, "left": None, "right": None}
#         }

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:  #BinarySearchTree
    def __init__(self):
        self.root = None


my_tree = BST()
print(my_tree.root)
