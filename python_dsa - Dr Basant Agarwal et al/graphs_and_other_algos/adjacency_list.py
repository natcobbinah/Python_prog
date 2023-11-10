# using a dictionary to represent the undirected  graph
# in the graphExample image, as an (Adjacency List)

graph = {}
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'C', 'E']
graph['C'] = ['A', 'B', 'E', 'F']
graph['E'] = ['B', 'C']
graph['F'] = ['C']
