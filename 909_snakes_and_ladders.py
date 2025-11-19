from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        q = deque()
        visited = set()
        q.append(1)
        visited.add(1)
        numSteps = 0

        def getRowCol(num):
            row = (num - 1) // n
            col = (num - 1) % n
        
            if row % 2 == 1:
                col = n - 1 - col
            row = n - 1 - row
            return (row, col)

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr == len(board) * len(board):
                    return numSteps
                
                for j in range(curr + 1, min(curr + 6, len(board) * len(board)) + 1):
                    r, c = getRowCol(j)

                    destination = board[r][c] if board[r][c] != -1 else j
                    if destination in visited:
                        continue
                    visited.add(destination)
                    q.append(destination)          
            numSteps += 1
        
        return -1
