"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque()
        q.append((root, 1))
        while q and root:
            node = q.popleft()
            if q and node[1] == q[0][1]:
                node[0].next = q[0][0]
            if node[0].left:
                q.append((node[0].left, node[1]+1))
            if node[0].right:
                q.append((node[0].right, node[1]+1))
        return root
    
class Solution: # O(1) space
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        ret = root
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next
        return ret