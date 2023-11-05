from bst import Tree

tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(9)
tree.insert(1)

for i in range(1,10):
    found = tree.search(i)
    print(f"{found} found")

max_val = tree.find_max()
print(f"maxVal = {max_val}")

min_val = tree.find_min()
print(f"minVal = {min_val}")

tree.remove(2)
print(tree.search(9))