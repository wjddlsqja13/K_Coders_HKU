# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """       
        def bfs(node):
            if not node: return 0

            v = node.val + bfs(node.left) + bfs(node.right)
            self.ans[v] += 1

            return v
            
        self.ans = collections.Counter()
        bfs(root)
        freq = self.ans.most_common(1)[0][1]
        return [x[0] for x in self.ans.most_common() if x[1] == freq]