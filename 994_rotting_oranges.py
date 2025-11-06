from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isValid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1
        
        time = countFresh = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    countFresh += 1

        while q:
            didInfect = False
            for _ in range(len(q)):
                currX, currY = q.popleft()
    
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    if isValid(currX + dx, currY + dy):
                        countFresh -= 1
                        grid[currX + dx][currY + dy] = 2
                        didInfect = True
                        q.append((currX + dx, currY + dy))    
            time += didInfect
        
        return time if countFresh == 0 else -1
