from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        q = deque([(0, 0)])
        parents = {}
        sol = 0
        n, m = len(grid), len(grid[0])
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == n - 1 and c == m - 1:
                    # Get path also 
                    # curr = (r, c)
                    # path = []
                    # while curr != (0, 0):
                    #     path.append(curr)
                    #     curr = parents[curr]
                    # path.append(curr)
                    # path.reverse()
                    # print(path)
                    return sol + 1
                
                grid[r][c] = 1
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                    if 0 <= r + dx < n and 0 <= c + dy < m and grid[r + dx][c + dy] == 0:
                        grid[r + dx][c + dy] = 1
                        # parents[(r + dx, c + dy)] = (r, c)
                        q.append((r + dx, c + dy))
            sol += 1
        return -1
