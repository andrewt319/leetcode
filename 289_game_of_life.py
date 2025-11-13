class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """        
        # -1 = current 0 that will turn into 1
        # 2 = current 1 that will turn into 0

        def getNumLiveNeighbors(r, c):
            numLiveNeighbors = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i, j) != (r, c) and (board[i][j] == 1 or board[i][j] == 2):
                        numLiveNeighbors += 1
            return numLiveNeighbors

        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                numLiveNeighbors = getNumLiveNeighbors(i, j)
                if board[i][j] == 1 and (numLiveNeighbors < 2 or numLiveNeighbors > 3):
                    board[i][j] = 2
                elif board[i][j] == 0 and numLiveNeighbors == 3:
                    board[i][j] = -1
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0

