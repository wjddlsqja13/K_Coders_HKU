# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        lh, rh = self.getHeight(root.left), self.getHeight(root.right)
        if abs(lh - rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
        
    def getHeight(self, root) -> int:
        if root == None:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1