"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueu the starting Vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # Create and empty set to store visited vertices
        visited = set()
        # While the queue is not empty..
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visiited
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
         # Create an empty stack and push the starting Vertex ID
        s = Stack()
        s.push(starting_vertex)
         # Create an empty set to store visited vertices
        visited = set()
         # While the stack is not empty..
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If that vertex has not been visiited...
            if v not in visited:
            # Mark it as visited...
                print(v)
                visited.add(v)
             # Then push all of its neighbors to the top of the stack
            for neighbor in self.vertices[v]:
                s.push(neighbor)
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # if visited = None (its at beginning of operation)
        # if visited is None:
        #     visited = set()
        # # Add starting vertex on initialization
        # visited.add(starting_vertex)
        # #For each connected vertex, minus those that have been visited, recursively call func
        # for neighbor in self.vertices[starting_vertex] - visited:
        #     self.dft_recursive(neighbor, visited)
        # print(visited)

         # Check if visited has been initialized
        if visited is None:
            # If not, initialize to an empty set
            visited = set()
        # Mark the node as visited
        print(starting_vertex)
        visited.add(starting_vertex)
        # Call DFT recursive on each neighbor that has not been visited
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
                # Create an empty queue and enqueu the starting Vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create and empty set to store visited vertices
        visited = set()
        # While the queue is not empty..
        while q.size() > 0:
            # Dequeue the first vertex
            path = q.dequeue()
            # If that vertex has not been visiited
            v = path[-1]
            if v not in visited:
                # Mark it as visited
                if v == destination_vertex:
                    return path
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty queue and enqueu the starting Vertex ID
        s = Stack()
        s.push([starting_vertex])
        # Create and empty set to store visited vertices
        visited = set()
        # While the stack is not empty..
        while s.size() > 0:
            # Dequeue the first PATH
            path = s.pop()
            # If that vertex has not been visiited
            v = path[-1]
            if v not in visited:
                # Mark it as visited
                if v == destination_vertex:
                    return path
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    s.push(path_copy)


    def dfs_recursive(self, starting_vertex, target_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Init visited
        if visited is None:
            visited = set()
        # Init path
        if path is None:
            path = []
        visited.add(starting_vertex)
        # Add vertex to the path
        path = path + [starting_vertex]
        # If we are at the target value, return the path
        if starting_vertex == target_vertex:
            return path
        # Otherwise, call DFS_recursive on each unvisited neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, target_vertex, visited, path)
                if new_path is not None:
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
    # print(graph.vertices)

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft(1)
    graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
