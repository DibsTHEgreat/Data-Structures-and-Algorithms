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
    
    # remove an edge in the existing dictionary list. Similar to the
    # add_edge function is a multi-step process.
    def remove_edge(self, vertex1, vertex2):
        # Simple edge case we can include is if vertex 1 and vertex 2
        # exist in the given list.
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            # another edge case we have is trying to run this code when
            # the 2 selected vertices do not have a edge between them.
            # What we can do is try to run the code, and if we run into an
            # error, we can ignore the error, and just return true
            try:
                # first we remove the edge between vertex 1 and vertex 2
                self.adj_list[vertex1].remove(vertex2)
                # now we remove the edge between vertex 2 and vertex 1.
                # It's important to remember that this connection needs to 
                # be severed from both ends.
                self.adj_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        # if the condition fails we return false
        return False
        
    # this function removes a vertex from a graph. In order to remove
    # a vertex all we have to do is remove all edges connecting to that
    # vertex and than we can remove the vertex.
    def remove_vertex(self, vertex):
        # Edge Case: Checking if given vertex exists
        if vertex in self.adj_list.keys():
            # Since our graphs are bi-directional, one of the benefits
            # is that whatever list is in vertex also points back to the
            # vertex. In this line of code, we're going through a list
            # of edges associated with D.
            for other_vertex in self.adj_list[vertex]:
                # Using the other_vertex we can remove the edge pointing
                # towards the inputted vertex.
                self.adj_list[other_vertex].remove(vertex)
            # once we have finished iterating through the entire list,
            # it is safe to delete the vertex since there are no edges
            # pointing towards it.
            del self.adj_list[vertex]
            return True
        # if the if-condition fails we return False
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

print('')
print('Now we will create a triangle and than severe')
print('an edge between 2 vertices. First we add vertex C')
print('than we create the edges between these 3 vertices.')

# adding vertex C to the graph
myGraph.add_vertex('C')

# creating an edge between vertex B and C.
myGraph.add_edges('B', 'C')

# creating an edge between vertex B and C.
myGraph.add_edges('C', 'A')

print('')
print('This is the new graph after adding vertex C.')
myGraph.print_graph()

print('')
print('Now we can test out the remove edge function by')
print('removing the connection between A & B')
myGraph.remove_edge('A', 'B')

print('')
print('Here are the new results from using the remove_edge function.')
myGraph.print_graph()

print('')
print('Now we can test out the remove edge function by')
print('removing the vertex D. First we need to create a new graph,')
print('containing vertices of A, B, C, D')

# Creating a new graph
myGraph2 = Graph()

# adding all the vertices
myGraph2.add_vertex('A')
myGraph2.add_vertex('B')
myGraph2.add_vertex('C')
myGraph2.add_vertex('D')

# adding all the edges
myGraph2.add_edges('A', 'B')
myGraph2.add_edges('A', 'C')
myGraph2.add_edges('A', 'D')
myGraph2.add_edges('B', 'D')
myGraph2.add_edges('C', 'D')

print('')
print('Here is the new graph:')
myGraph2.print_graph()

print('')
print('Now we can test out the remove vertex function by removing vertex D')
myGraph2.remove_vertex('D')

print('')
print('Here are the results after using the remove_vertex function:')
myGraph2.print_graph()