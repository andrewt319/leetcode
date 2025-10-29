# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        sol = []
        q = deque()
        q.append(root)

        while q:
            numNodesInLayer = len(q)
            for i in range(numNodesInLayer):
                curr = q.popleft()
                if i == numNodesInLayer - 1:
                    sol.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return sol
                


