# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root :
            return 0
        
        return self.dfs(root, targetSum) + self.pathSum(root.left,targetSum) + self.pathSum(root.right, targetSum)
        
        
    def dfs(self,root, targetSum):
        count = 0
        if not root : 
            return 0
            
        if root.val == targetSum :
            count += 1
                
        count += self.dfs(root.left , targetSum - root.val) + self.dfs(root.right, targetSum - root.val)
            
        return count