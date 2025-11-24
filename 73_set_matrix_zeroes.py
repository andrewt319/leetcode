class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        doesFirstRowHaveZero = doesFirstColHaveZero = False

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i == 0:
                        doesFirstRowHaveZero = True
                    if j == 0:
                        doesFirstColHaveZero = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(n - 1, 0, -1):
            for j in range(m - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if doesFirstColHaveZero:
            for i in range(n):
                matrix[i][0] = 0
        
        if doesFirstRowHaveZero:
            for j in range(m):
                matrix[0][j] = 0

