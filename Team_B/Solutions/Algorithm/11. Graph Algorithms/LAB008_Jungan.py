# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def dfs(root,isLeft):
            if not root: 
                return
            if isLeft and not root.left and not root.right:
                self.sum += root.val
            dfs(root.left,1)
            dfs(root.right,0)
        
        dfs(root,0)
        return self.sum
        