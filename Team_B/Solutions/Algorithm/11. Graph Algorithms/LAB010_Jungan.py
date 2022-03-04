# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        subtree_sum = defaultdict(int)
        output = []
        
        def dfs(node) :
            if not node:
                return 0 
            
            sum = node.val + dfs(node.left) + dfs(node.right)
            
            subtree_sum[sum] += 1
            
            return sum
        
        dfs(root)
        highest_freq = max(subtree_sum.values())
        
        for i in subtree_sum :
            if subtree_sum[i] == highest_freq :
                output.append(i)
        
        return output