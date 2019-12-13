
from util import Stack, Queue
def earliest_ancestor(ancestors, starting_node):

    def get_parents(node):
        # Get parents function:
        # test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
        # Loop through ancestors data, put each parent of current child into an array
        parents = []
        for ancestor in ancestors:
            if ancestor[1] == node:
                parents.append(ancestor[0])
        return parents

    # Return -1 if input has no parents
    if len(get_parents(starting_node)) == 0:
        return -1

    paths = []
    def find_paths(ancestors, starting_vertex, path=None):
        # find_furthest_ancestor function:
        # If input has no parents, return -1, (loop through data set, find if there are any tuples with input as second value )
        # else
        # If the farthest ancestors are the same distance away, return the smaller one
        # Create an empty queue and enqueu the starting Vertex ID

        if path is None:
            path = []
        path = path + [starting_vertex]
        parents = get_parents(starting_vertex)

        if len(parents) == 0:
            paths.append(path)
        else:
            for parent in parents:
                find_paths(ancestors,parent,path)


    # Invoke find Paths
    find_paths(ancestors,starting_node)

    # Assign Longest Path and (If has one) It's Tie
    longest_path_len = 0
    longest_path = []
    tied_path = []

    for path in paths:
        if len(path) > longest_path_len:
            longest_path = path
            longest_path_len = len(path)
        elif len(path) == longest_path_len:
            tied_path = path

    # Return path with smaller oldest ancestor
    if len(tied_path) == 0:
        return longest_path[-1]
    elif longest_path[-1] > tied_path[-1]:
        return tied_path[-1]
    else:
        return longest_path[-1]



# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# earliest_ancestor(test_ancestors, 1)




#       q = Queue()
    #     q.enqueue([starting_vertex])
    #     # Create and empty set to store visited vertices
    #     visited = set()
    #     # While the queue is not empty..
    #     while q.size() > 0:
    #         # Dequeue the first vertex
    #         path = q.dequeue()
    #         # If that vertex has not been visiited
    #         v = path[-1]
    #         if v not in visited:
    #             # Mark it as visited
    #             visited.add(v)
    #             # Then add all of its neighbors to the back of the queue
    #             parents = get_parents(v)
    #             for parent in parents:
    #                 path_copy = path.copy()
    #                 path_copy.append(neighbor)
    #                 q.enqueue(path_copy)
    # # print(find_paths(ancestors, starting_node))
    #     return -1