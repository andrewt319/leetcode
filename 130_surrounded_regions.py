class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r, c):
            if not isValid(r, c):
                return False
            visited.add((r, c))
            isConnectedToEdge[r][c] = True
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if isValid(r + dx, c + dy):
                    dfs(r + dx, c + dy)
        
        def isValid(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0]) and (r, c) not in visited and board[r][c] == 'O'

        isConnectedToEdge = [[False for i in range(len(board[0]))] for j in range(len(board))]
        visited = set()
        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)
        
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board) - 1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if isConnectedToEdge[i][j] == False and board[i][j] == 'O':
                    board[i][j] = 'X'

