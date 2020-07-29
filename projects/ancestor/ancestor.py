# import sys
# sys.path.insert(0, '../graph')
from util import Queue, Stack
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # s = Stack()
    # s.push([starting_node])

    # visited = set()

    #create a graph
    g = Graph()

    for ancestor in ancestors:
        parent = ancestor[0]
        child = ancestor[1]

        #Creating the vertices
        g.add_vertex(parent)
        g.add_vertex(child)

        #Add the edges
        g.add_edge(child, parent)


    # print(g.verticies)
    s = Stack()  # TODO
    #Add starting vertice to the stack
    s.push([starting_node])
    #Will be constantly updating itself to have the correct path
    ancestor_path = []
    visited = set()

    while s.size() > 0:
        path = s.pop()
        print(path)
        #Get the last veritice from the path
        last_vertice = path[-1]
        
        #Check to see if it's the destination vertex
        if last_vertice == ancestor:
            return path
        
        if last_vertice not in visited:
            if len(path) > len(ancestor_path):
                ancestor_path = path
            visited.add(last_vertice)
                
            if len(path) == len(ancestor_path):
                if path[-1] < ancestor_path[-1]:
                    ancestor_path = path

            #Add a path to all the neighbors in the stack
            for neighbor in g.get_neighbors(last_vertice):
                path_copy = path.copy()
                path_copy.append(neighbor)
                s.push(path_copy)
    if len(ancestor_path) == 1:
        return -1
    return ancestor_path[-1]
             



        # print(ancestor)

    
    
    #If the input individual has no parents return -1:

    #If the input individual has more than one ancestor tied for 'earliest' return the ancestor with the lowest numeric ID

    #Return the 'ancestor' the furthest away from the input individual