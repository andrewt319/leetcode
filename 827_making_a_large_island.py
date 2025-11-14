class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        colorToSize = {0:0}
        color = 2
        sol = 0
        n, m = len(grid), len(grid[0])

        def dfs(r, c, color):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1):
                return 0
            
            grid[r][c] = color
            size = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                size += dfs(r + dx, c + dy, color)
            return size
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    colorToSize[color] = dfs(i, j, color)
                    sol = max(sol, colorToSize[color])
                    color += 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    continue

                up = grid[i - 1][j] if i > 0 else 0
                left = grid[i][j - 1] if j > 0 else 0
                right = grid[i][j + 1] if j < m - 1 else 0
                south = grid[i + 1][j] if i < n - 1 else 0
                colors = set([up, left, right, south])

                islandSize = 1
                for color in colors:
                    islandSize += colorToSize[color]
                sol = max(islandSize, sol)
        return sol
            

