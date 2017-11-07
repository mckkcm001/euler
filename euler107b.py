from collections import deque

tree = {'a': ['b', 'c', 'd'],
        'b': ['a', 'd', 'e'],
        'c': ['a', 'd', 'f'],
        'd': ['a', 'b', 'c', 'e', 'f', 'g'],
        'e': ['b', 'd', 'g'],
        'f': ['c', 'd', 'g'],
        'g': ['f', 'd', 'e']
}

def children(token, tree):
    "returns a list of every child"
    visited = set()
    to_crawl = deque([token])
    while to_crawl:
        current = to_crawl.popleft()
        if current in visited:
            continue
        visited.add(current)
        node_children = set(tree[current])
        to_crawl.extend(node_children - visited)
    return list(visited)

print children('g',tree)