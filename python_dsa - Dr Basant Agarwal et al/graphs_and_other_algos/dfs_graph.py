# using a dictionary to represent the undirected graph in 
# the graphnetwork 2.png image, the (Adjacency list) representation is
graph = {}
graph['A'] = ['B','S']
graph['B'] = ['A']
graph['S'] = ['C','G']
graph['D'] = ['C']
graph['G'] = ['S','F','H']
graph['H'] = ['G','E']
graph['F'] = ['C','G']
graph['C'] = ['D','S','E','F']