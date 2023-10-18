# Doubly Linked List
# They have pointers pointing towards the previous nodes

# Creates a node one pointing towards the next node and one pointing
# towards the previous node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# class containing functions to create and manipulate doublyLinkedList
class DoublyLinkedList:
    #Constructor for the class
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    #prints the list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    
    
# this is how we call the constructor in our code
my_DLL = DoublyLinkedList(7)

my_DLL.print_list()

