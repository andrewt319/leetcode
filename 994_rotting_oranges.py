from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        numFreshOranges = time = 0
        n, m = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    numFreshOranges += 1
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if grid[r][c] == 1:
                    numFreshOranges -= 1
                    grid[r][c] = 2
                if numFreshOranges == 0:
                    return time

                for dx, dy in directions:
                    if 0 <= r + dx < n and 0 <= c + dy < m and grid[r + dx][c + dy] == 1:
                        q.append((r + dx, c + dy))
            time += 1

        return -1 if numFreshOranges > 0 else 0
