# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sol = -1

        def dfs(node):
            nonlocal k
            nonlocal sol
            if not node or k == 0:
                return
            
            dfs(node.left)
            k -= 1
            if k == 0:
                sol = node.val
                return
            dfs(node.right)
        
        dfs(root)
        return sol

