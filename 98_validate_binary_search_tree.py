# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, greaterThan, lessThan):
            if not node:
                return True
            
            if not (greaterThan < node.val < lessThan):
                return False

            return dfs(node.left, greaterThan, min(lessThan, node.val)) and dfs(node.right, max(greaterThan, node.val), lessThan)
        
        return dfs(root.left, float('-inf'), root.val) and dfs(root.right, root.val, float('inf'))
        

