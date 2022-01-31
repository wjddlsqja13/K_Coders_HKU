def has_cycle(head):
    visited = set()
    node = head
    while node:
        i = id(node)
        if i in visited:
            return 1
        visited.add(i)
        node = node.next
    return 0