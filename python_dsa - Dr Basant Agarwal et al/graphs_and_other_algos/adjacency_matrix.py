"""Adjacency List Representation of graphExample image"""
graph = {}
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'C', 'E']
graph['C'] = ['A', 'B', 'E', 'F']
graph['E'] = ['B', 'C']
graph['F'] = ['C']

# constructing the adjacency matrix from the adjacency list above, we have
matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)

adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
edges_list = []

# filling up the multi-dimensional array
for key in matrix_elements:
    for neighbor in graph[key]:
        edges_list.append((key,neighbor))

print(edges_list)

# filling up our adjacency-matrix
for edge in edges_list:
    index_of_first_vertex = matrix_elements.index(edge[0])
    index_of_second_vertex = matrix_elements.index(edge[1])
    adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1


print()

print(adjacency_matrix)