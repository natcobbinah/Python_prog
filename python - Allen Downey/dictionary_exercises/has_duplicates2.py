def has_duplicates2(t):
    return len(set(t)) < len(t)

t = 'abb'
print(has_duplicates2(t))