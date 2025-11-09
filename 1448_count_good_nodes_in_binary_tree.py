# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        sol = 0
        def dfs(node, maximum):
            nonlocal sol
            if not node:
                return    
            if node.val >= maximum:
                sol += 1
            
            maximum = max(maximum, node.val)
            dfs(node.left, maximum)
            dfs(node.right, maximum)
        
        dfs(root, float('-inf'))
        return sol
