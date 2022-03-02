# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        s = [root]
        ans = 0
        while s:
            node = s.pop()
            if node == None:
                continue
            if node.left != None:
                if node.left.left == None and node.left.right == None:
                    ans += node.left.val
            s.append(node.left)
            s.append(node.right)
        return ans
        