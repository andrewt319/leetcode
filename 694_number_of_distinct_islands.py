class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        unique = set()
        n, m = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1):
                return ''
            
            grid[r][c] = 0
            currStr = ''

            currStr += 'n' + dfs(r - 1, c)
            currStr += 'w' + dfs(r, c - 1)
            currStr += 'e' + dfs(r, c + 1)
            currStr += 's' + dfs(r + 1, c)

            return currStr
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    islandHash = dfs(i, j)
                    unique.add(islandHash)
        
        return len(unique)
