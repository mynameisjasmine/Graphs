"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy.

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check to see if the vertices exist in the graph
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist in graph') # TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]  # TODO

    
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()  # TODO
        
        #Add starting node to the queue by appending the value to the self.queue array
        q.enqueue(starting_vertex)
        
        #Keep track of visited vertices by creating an empty set
        visited = set()
        
        #While the self.queue array is not empty
        while q.size() > 0:
            #Storing the value of the popped vertice into a variable
             value = q.dequeue()

             #If not visited, (ie if the value that's been popped has not been added to the visited set)
             if value not in visited:
                 #print the value
                 print(value)
                 #Mark as visited (ie add the popped value to the visited set)
                 visited.add(value)

              # Add all unvisited neighbors to the queue
                 for next_vertice in self.get_neighbors(value):
                        q.enqueue(next_vertice)





    


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        #Add a starting node to the stack  # TODO
        s.push(starting_vertex)
        
        #Keep track of visited vertices by creating an empty set
        visited = set()

         #While the stack is not empty
        while s.size() > 0:
            value = s.pop()
            #If the vertice has not been visited (ie added to the visited set)
            if value not in visited:
                #Print the value of the vertice
                print(value)
                #Mark vertice as visited (i.e add the value to the visited set)
                visited.add(value)

                #Push all unvisited neighbors to the stack
                for next_neighbor in self.get_neighbors(value):
                    s.push(next_neighbor)
             



    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        
        if starting_vertex in visited:
            return 
        else:
            visited.add(starting_vertex)
            print(starting_vertex)

            for neighbor in self.get_neighbors(starting_vertex):
                if neighbor not in visited:
                    self.dft_recursive(neighbor, visited)

      #Trying to do this using the stack


        # s = Stack()   # TODO
        # s.push(starting_vertex)
        # visited = set()
        
        # #base case
        # if s.size() == 0:
        #     return
        
        # value = s.pop()
        # if value not in visited:
            
        #     visited.add(value)
        #     print(value)
        #     for neighbor in self.get_neighbors(value):
        #         if neighbor not in visited:
        #             self.dft_recursive(neighbor)
        #         s.push(neighbor)

        
        # if s.size() > 0:
        #     self.dft_recursive(value)




    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        
        q = Queue()  # TODO
        #Add starting vertice to the queue
        q.enqueue([starting_vertex])

        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            #Get the last vertex from the path
            last_vertice = path[-1]
            
            if last_vertice == destination_vertex:
                return path

            #Check to see if it's been visited
            if last_vertice not in visited:
                visited.add(last_vertice)

                for neighbor in self.get_neighbors(last_vertice):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)
            


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()  # TODO
        #Add starting vertice to the stack
        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            path = s.pop()
            #Get the last veritice from the path
            last_vertice = path[-1]
            
            #Check to see if it's the destination vertex
            if last_vertice == destination_vertex:
                return path
            
            if last_vertice not in visited:
                visited.add(last_vertice)

                #Add a path to all the neighbors in the stack
                for neighbor in self.get_neighbors(last_vertice):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        print(starting_vertex)  # TODO

        if visited is None:
            visited = set()
        if path is None:
            path = []
        
        visited.add(starting_vertex)
        path = path + [starting_vertex] #This makes a copy and creates a new list

        #Base case
        if starting_vertex == destination_vertex:
            return path
        
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)

                if new_path:
                    return new_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
