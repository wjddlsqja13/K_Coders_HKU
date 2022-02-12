# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #function to get height
    def height(self,node) :
        #current subtree's height is 0
        if not node:
            return 0
        
        left = self.height(node.left)
        right = self.height(node.right)
        
        
        if abs(left-right) < 2 :
            return max(left,right) + 1 
        else :
            self.balanced = False
            return 0
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.height(root)
        return self.balanced