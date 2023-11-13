# using a dictionary to represent the undirected graph in 
# the graphnetwork 2.png image, the (Adjacency list) representation is
graph = {}
graph['A'] = ['B','S']
graph['B'] = ['A']
graph['S'] = ['C','G']
graph['D'] = ['C']
graph['G'] = ['S','F','H']
graph['H'] = ['G','E']
graph['E'] = ['C','H']
graph['F'] = ['C','G']
graph['C'] = ['D','S','E','F']

def depth_first_search(graph,root):
    visited_vertices = []
    graph_stack = []

    graph_stack.append(root)
    node = root

    while len(graph_stack) > 0:
        if node not in visited_vertices:
            visited_vertices.append(node)
        adjacent_nodes = graph[node]
        
        if set(adjacent_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
            if len(graph_stack) > 0:
                node = graph_stack[-1]
            continue 
        else:
            remaining_elements = set(adjacent_nodes).difference(set(visited_vertices))

            first_adjacent_node = sorted(remaining_elements)[0]
            graph_stack.append(first_adjacent_node)
            node = first_adjacent_node
    return visited_vertices

print(depth_first_search(graph,'A'))