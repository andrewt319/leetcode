import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        sol = []
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            pq.append((distance, x, y))
        
        heapq.heapify(pq)
        while k > 0:
            _, x, y = heapq.heappop(pq)
            sol.append([x, y])
            k -= 1

        return sol
