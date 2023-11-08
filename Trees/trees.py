# In this file I am creating a Binary Search Tree

# First we create class Node that will go into the Binary Search Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Important to note that when we add a node it technically points to nothing

# Here is code for the class Binary Search Tree
class BinarySearchTree:
# the constructor creates an empty BST
    def __init__(self, value):
        self.root = None
    