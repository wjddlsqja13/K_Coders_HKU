from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue = deque([(p,q)])
        
        while queue:
            n1, n2 = queue.popleft()
            
            if (n1 != None and n2 != None):
                if n1.val != n2.val:
                    return False
                queue.append((n1.left, n2.left))
                queue.append((n1.right, n2.right))
                
            elif (n1 == None and n2 == None):
                pass
            else:
                return False
        return True
