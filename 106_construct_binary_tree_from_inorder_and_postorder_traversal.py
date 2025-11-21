# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = {c:i for i,c in enumerate(inorder)}
        def helper(l, r):
            if l >= r or not postorder:
                return None
            
            rootVal = postorder.pop()
            root = TreeNode(rootVal)

            inorderRootIdx = inorderIdx[rootVal]
            root.right = helper(inorderRootIdx + 1, r)
            root.left = helper(l, inorderRootIdx)
            return root

        return helper(0, len(inorder))
