from collections import deque

# To use BFS to traverse this graph, we will make use of a queue
# In the wors-case scenario, each vertex or node and edge will be traversed
# thus the time complexity of BFS algorithm is O(|V| + |E|), where
# |V| = number of vertices or nodes and |E| = number of edges in the graph


def breadth_first_search(graph, root):
    visited_vertices = list()
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


# Te
