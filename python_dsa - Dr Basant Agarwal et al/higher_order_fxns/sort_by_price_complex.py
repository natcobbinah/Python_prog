items = [
    ['rice', 2.4, 8],
    ['flour', 1.9, 5],
    ['corn', 4.7, 6]
]

items.sort(key=lambda n: n[1])
print(items)