# In this file I will be creating a class for the data structure known as
# graphs using adjacency lists.
class Graph:
    # Constructor for the graph class, all I'm doing is creating an empty
    # dictionary.
    def __init__(self):
        self.adj_list = {}
    
    # Adding vertices into the dictionary list
    def add_vertex(self, vertex):
        # we need to make sure that duplicates are not added onto 
        # the graph
        if vertex not in self.adj_list.keys():
            # adding vertex
            self.adj_list[vertex] = []
            return True
        # we only do this if our if condition failed
        return False
    
    # Adding edges into the dictionary list.
    # Multi-step process of first adding the vertex
    # into the list and than connecting them to the vertices
    def add_edges(self, vertex1, vertex2):
        # First edge case is when both vertices exist and all
        # we want to do is connect two existing vertices. To
        # check for this all we have to do is create a if 
        # statement checking for if vertex1 and vertex2 are in 
        # the list.
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            # First we append the new vertex onto the first vertex
            # or what ever it needs to connect to.
            self.adj_list[vertex1].append(vertex2)
            # Now we finish the connection by switching the command
            # appending the old vertex to the new vertex.        
            self.adj_list[vertex2].append(vertex1)
            return True
        # Impossible to add edges between 2 vertices when either one or
        # both don't exist in the list.
        return False
        
        
    # this function prints out the graph list 
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])


print('In this file we are testing out the graph function.')
# creating an empty list
myGraph = Graph()

print('')
print('First we will add the vertex A into the graph.')
print('')

# adding a vertex to the graph
myGraph.add_vertex('A')

# printing out my graph
myGraph.print_graph()

print('')
print('Now we are testing the add edge function. By adding one')
print('more vertex B, and creating an edge between A & B.')

# adding another vertex to the graph
myGraph.add_vertex('B')

# creating an edge between vertex A and B.
myGraph.add_edges('A', 'B')

print('')
print('Here are the printed results of the add edge function.')
myGraph.print_graph()