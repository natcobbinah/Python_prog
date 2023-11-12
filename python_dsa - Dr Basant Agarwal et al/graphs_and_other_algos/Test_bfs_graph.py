from bfs_graph import breadth_first_search

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

breadth_first_search(graph, graph['A'])