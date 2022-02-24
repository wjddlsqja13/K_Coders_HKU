# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #use of queue
        if root is None :
            return 
        
        queue = deque([root])
        output = []
        
        while(len(queue) > 0):
            levels = []
            
            for i in range(len(queue)) : 
                
                node = queue.popleft()

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)
                
                levels.append(node.val)
            output.append(levels)
        return output
        