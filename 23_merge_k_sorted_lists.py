# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        sol = curr = ListNode()

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(pq, (node.val, i, node))

        while pq:
            _, i, node= heapq.heappop(pq)
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))
            curr.next = node
            curr = curr.next
        return sol.next
