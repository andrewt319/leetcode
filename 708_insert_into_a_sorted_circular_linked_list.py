"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head

        
        tmp = head.next
        while tmp != head:
            if tmp.val <= insertVal <= tmp.next.val or (tmp.next.val < tmp.val and (insertVal < tmp.next.val or insertVal > tmp.val)):
                break
            tmp = tmp.next
        
        node = Node(insertVal, tmp.next)
        tmp.next = node
        return head
