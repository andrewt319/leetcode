from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        sol = []

        for frm, to in tickets:
            heapq.heappush(adjList[frm], to)
        
        def dfs(airport):
            while adjList[airport]:
                dfs(heapq.heappop(adjList[airport]))
            sol.append(airport)

        dfs('JFK')
        return sol[::-1]

