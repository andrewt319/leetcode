import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def isValid(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in visited
        
        pq = [(grid[0][0], 0, 0)]
        visited = set()
        sol = 0

        while pq:
            elevation, r, c = heapq.heappop(pq)
            visited.add((r, c))
            sol = max(sol, elevation)

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return sol
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if isValid(r + dx, c + dy):
                    heapq.heappush(pq, (grid[r + dx][c + dy], r + dx, c + dy))
        
        return -1
