# Fun fact: Prime numbers increase the randomness for how the key value
# pairs would be distributed throughout the hash table. There by also
# reducing the chances of a collision.
class HashTable:
    # For my file I'm going to make my constructor build an empty list
    # from 0 to 6
    def __init__(self, size = 7):
        # Creates a list of 7 items containing a value of None
        self.data_map = [None] * size
    
    # Hash function
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # we do ord(letter) to get the ASCII number for each letter.
            # For my example I am using 23, but that constant can be 
            # replaced with any prime number. Than we use a mod operator
            # to divide our numbers by the length of the dataset
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    # Print function
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
            
    # The Set function for the Hash table
    def set_items(self, key, value):
        # First we figure out the address for where
        # we will store the key value pair, by using
        # the hash function
        index = self.__hash(key)
        # taking that index we than initialize an empty 
        # list at that specific address. We only do this
        # if there already isn't a list at the address.
        # Our if statement uses None, since our Hash table
        # is initially created with all values being None
        if self.data_map[index] == None:
            self.data_map[index] = []
        # Now that we have created an empty list at a specific
        # address, we can add our key value pair into the hash
        # table. We use .append since technically our list is a
        # linked list.
        self.data_map[index].append([key, value])
    
    # The Get function for the Hash Table
    def get_item(self, key):
        # We take our key, and use the hash function to find 
        # the index within our list.
        index = self.__hash(key)
        # To save time, we only want to run these lines of code,
        # if the index actually has values, as in it is not
        # equal to None.
        if self.data_map[index] is not None:
            # Now we iterate through the list at that 
            # particular index. Remember, sometimes
            # indexes will have more than one key value pair,
            # this happens through a process of seperate
            # chaining, usually done to avoid collisions.
            for i in range(len(self.data_map[index])):
                # this might look complex but it really isn't.
                # we take the same index, and the variable i 
                # is what is being iterated through the list
                # at that particular index. At each given list
                # location, our key value pairs have 2 values, a
                # key and a value, and are in the form: ['Ex', ####]
                # Thus in order to compare our values with the
                # user inputted key, we have to look at the [0]
                # location, as in the first value in the key value pair.
                if self.data_map[index] [i] [0] == key:
                    # goal of the function is to return the value
                    # at the index, so instead of returning [0]
                    # which is a key, we return [1] which is a value.
                    return self.data_map[index] [i] [1]
        # If index is equal to None, than the only thing we can 
        # return is the value None at that specific index.
        return None
        
    
# Creating my example Hash table
exHashTable = HashTable()

print('Below is the printed results of the default constructor for Hash Table Class.')

exHashTable.print_table()

print('')
print('Now I will test out the set function.')
print('')
print('First we will input the key value pair: Zekrom: 644')
exHashTable.set_items('Zekrom', 644)
print('')
print('Than we will input the key value pair: Reshiram: 643')
exHashTable.set_items('Reshiram', 643)
print('')
print('Lastly we will input the key value pair: Kyurem: 646')
exHashTable.set_items('Kyurem', 646)

print('')
print('Below is the printed results of the set function for Hash Table Class.')

exHashTable.print_table()

# Now it is time to test out the get item function
print('')
print('Below contains results form our get_item function.')
print('')
print('Get item, Zekrom: ', exHashTable.get_item('Zekrom'))
print('Get item, Reshiram: ', exHashTable.get_item('Reshiram'))
# Testing out an edge case, what will happen if we input 
# a value not on the list?
print('Get item, Keldeo: ', exHashTable.get_item('Keldeo'))