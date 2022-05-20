graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}


def search_in_depth():
    pass


visited = []  # List to keep track of visited nodes.
queue = []   # Initialize a queue


def search_in_width(visited, graph, node):
    global queue
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
search_in_width(visited, graph, 'A')
