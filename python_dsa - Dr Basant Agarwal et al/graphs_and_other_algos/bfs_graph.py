from collections import deque

# using a dictionary to represent the undirected graph in 
# the graphnetwork 2.png image, the (Adjacency list) representation is
graph = {}
graph['A'] = ['B','D','G']
graph['B'] = ['E','F']
graph['C'] = ['F','H']
graph['D'] = ['A','F']
graph['E'] = ['B','G']
graph['F'] = ['B','C','D']
graph['G'] = ['A','E']
graph['H'] = ['C']

# To use BFS to traverse this graph, we will make use of a queue
# In the wors-case scenario, each vertex or node and edge will be traversed
# thus the time complexity of BFS algorithm is O(|V| + |E|), where
# |V| = number of vertices or nodes and |E| = number of edges in the graph
def breadth_first_search(graph, root):
    visited_vertices = []
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root

    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adjacent_nodes = graph[node]

        remaining_elements = set(adjacent_nodes).difference(
            set(visited_vertices))

        if len(remaining_elements) > 0:
            for elem in sorted(remaining_elements):
                visited_vertices.append(elem)
                graph_queue.append(elem)

    return visited_vertices


print(breadth_first_search(graph, 'A'))
