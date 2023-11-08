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
    def __init__(self):
        self.root = None
    
# this function is for inserting a node into a bst
    def insert(self, value):
        new_node = Node(value)
        # first edge case is if there is an empty bst
        if self.root is None:
            self.root = new_node
            return True
        # now we will create a variable that can traverse through
        # the BST, and can be used to compare with actual values
        # in the tree
        temp = self.root
        while (True):
            # cannot add a node with a value already in the BST
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

# Creating a function that locates and prints a user inputted node from the BST
    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
# Creating a BST            
bst = BinarySearchTree()

# Inserting values
bst.insert(2)
bst.insert(1)
bst.insert(3)

#Showcasing how our code works
print('Printing Out the Root Node:', bst.root.value)
print('Printing Out the Node Left of the Root Node:', bst.root.left.value)
print('Printing Out the Node Right of the Root Node:', bst.root.right.value)

# Creating a New BST
bst_2 = BinarySearchTree()
bst_2.insert(47)
bst_2.insert(21)
bst_2.insert(76)
bst_2.insert(18)
bst_2.insert(27)
bst_2.insert(52)
bst_2.insert(82)

print('Given this new BST, is the node 27 in it:', bst_2.contains(27))

print('Given this new BST, is the node 17 in it:', bst_2.contains(17))