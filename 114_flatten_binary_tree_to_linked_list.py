# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prevRight = None
        def dfs(root):
            nonlocal prevRight
            if not root:
                return root
            
            right = dfs(root.right)
            left = dfs(root.left)

            # the key is after you explore right and left, set the current node to the previous "right" node
            # in the example, think about how you need to connect 4 -> 5. from the left subtree, you need access
            # to that 5 somehow. that relation between the two is that it's the previous rihgt.
            # go right, then go left, then connect the current node.right to prevRight, and move the left to the right.
            root.right = prevRight
            prevRight = root
            root.left = None
            
            return root
        
        dfs(root)
        return root
