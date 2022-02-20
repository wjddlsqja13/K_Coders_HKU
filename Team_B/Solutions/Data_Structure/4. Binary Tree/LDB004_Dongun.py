# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root): # 0 if leaf, 1 if covered with camera, 2 if covered without camera
            if not root: return 2
            l, r = dfs(root.left), dfs(root.right)
            if l == 0 or r == 0:
                self.res += 1
                return 1
            elif l == 1 or r == 1:
                return 2
            else: return 0
        return (dfs(root) == 0) + self.res
            
                