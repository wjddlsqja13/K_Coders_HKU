# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None:
            return 0
        self.ans = 0
        self.dfs(root, targetSum)
        return self.ans
    
    def dfs(self, root, target):
        if root == None:
            return
        self.getSum(root, target)
        self.dfs(root.left, target)
        self.dfs(root.right, target)
    
    def getSum(self, root, target):
        if root == None:
            return
        if root.val == target:
            self.ans += 1
        self.getSum(root.left, target-root.val)
        self.getSum(root.right, target-root.val)