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
    # Main constructor for the DLL class
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    # prints the DLL
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    # adds a node to the DLL, also checks if the list is empty or not
    def append(self, value):            
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    # this function removes a node from a DLL, also known as 
    # the pop method. Edge cases: Only 1 node, and empty list
    def pop(self):
        if self.length == 0: # edge case for an empty list
            return None
        temp = self.tail
        if self.length == 1: # edge case for a 1 node DLL
            self.head = None
            self.tail = None
        else: # for normal DLL
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value 
    # note I am only keeping .value for testing purposes
    # it is better to return temp since that is the entire node
    
    # this function adds a node to the beginning of the DLL
    def prepend(self, value):
        new_node = Node(value)
        
        if self.length == 0: #edge case for an empty list
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    # this method will pop the first node in a DLL
    def pop_first(self):
        if self.length == 0: # checks if there is a empty lists
            return None
        temp = self.head
        if self.length == 1: # checks if there is only one node
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp.value
    # note: Same as the pop function I am only keeping
    # value for testing purposes it is better to return 
    # temp since that is the entire node
    
    # this function returns an item at a specific index
    def get(self, index):
        if index < 0 or index >= self.length: # making sure the index is a proper value
            return None
        temp = self.head
        if index < self.length/2: 
            # checking if the index is in the first half or second half
            # it helps with optimization for the code
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                # in this for loop we tell the code to start at the last node
                # which is self.length - 1, and than we tell the for loop to 
                # go down by 1 so we represent this by -1
                temp = temp.prev
        return temp
    # note: Same as the pop_first function I am only keeping
    # value for testing purposes it is better to return 
    # temp since that is the entire node
    
    # this function changes a value at a specific index
    def set_value(self, index, value):
        temp = self.get(index) 
        # makes our job easier, instead of rewriting our code
        if temp:
            temp.value = value
            return True
        else:
            return False
    
    # this function inserts a new node at a specified index with a inputted value
    def insert(self, index, value):
        if index < 0 or index > self.length: 
        # making sure the index is a proper value
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1
        return True

    # this function removes a node at a specified index
    def remove(self, index):
        if index < 0 or index >= self.length: 
        # making sure the index is a proper value
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
        
# this is how we call the constructor in our code
my_DLL = DoublyLinkedList(7)
print('Printing out a DLL after using the main constructor:')
my_DLL.print_list()
print('')

# this is how we call the append function in our code
my_DLL.append(2)
print('List updated after append method is used:')
my_DLL.print_list()
print('')

# this is how we call the pop function in our code
print('Testing out the pop function by removing Node 2:')
print(my_DLL.pop())

print('')
print('Printing out a DLL after using the pop function:')
my_DLL.print_list()

print('')
print('Testing out the pop function by removing Node 1:')
print(my_DLL.pop())

print('')
print('Printing out a DLL after using the pop function:')
my_DLL.print_list()

print('')
print('Testing out the pop function on an empty list:')
print(my_DLL.pop())

print('')
print('Printing out a DLL after using the pop function:')
my_DLL.print_list()

print('')
print('Resetting the DLL, here is the list before modifications')
my_DLL.append(2)
my_DLL.append(3)
my_DLL.print_list()
print('')

print('Testing out the prepend function by adding Node with a value of 1:')
print(my_DLL.prepend(1))

print('')
print('Printing out a DLL after using the prepend function:')
my_DLL.print_list()

print('')
print('Testing out the pop first function by removing the first node:')
print(my_DLL.pop_first())

print('')
print('Printing out a DLL after using the pop_first function:')
my_DLL.print_list()

print('')
print('Testing out the get function by printing the node at index 1:')
print(my_DLL.get(1))

print('')
print('Testing out the set function by changing the value at node index 1 from a 3 to a 4:')
print(my_DLL.set_value(1, 4))

print('')
print('Printing out the DLL after using the set function:')
my_DLL.print_list()

print('')
print('Testing out the insert function by adding a node at index 1:')
print(my_DLL.insert(1, 3))

print('')
print('Printing out the DLL after using the insert function:')
my_DLL.print_list()

print('')
print('Testing out the remove function by removing a node at index 2:')
print(my_DLL.remove(2))

print('')
print('Printing out the DLL after using the insert function:')
my_DLL.print_list()