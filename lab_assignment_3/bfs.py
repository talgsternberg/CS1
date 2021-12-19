#Tal Sternberg
#CS 1
#load_bfs.py for lab3: creates a breadth first search algorithm to implement in map_plot.py
#11/6/2019


from collections import deque


def bfs(start_vertex, end_vertex):
    queue = deque()
    queue.append(start_vertex)
    backtrack = {}
    backtrack[start_vertex] = None

    while len(queue) > 0:
        # remove vertex x
        x = queue.popleft()
        for neighbor in x.get_neighbors():
            if neighbor not in backtrack:

                #append to dictionary
                backtrack[neighbor] = x

                #add y to queue
                queue.append(neighbor)
    path = []
    while end_vertex != None:
        path.append(end_vertex)
        end_vertex = backtrack[end_vertex]

    return path

