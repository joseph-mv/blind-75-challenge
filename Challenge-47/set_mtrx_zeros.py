class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Set Matrix zeroes
            If an element in matrix is 0, set its entire row and column to 0's.
        Args:
            matrix:An m x n integer matrix matrix
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])      
        col_zero, row_zero=matrix[0][0], matrix[0][0]
        
        for i in range(m):
            for j in range(n):            
                if matrix[i][j]==0:
                    if i==0:
                        row_zero=0
                    if j==0:
                        col_zero=0
                    matrix[0][j]=0
                    matrix[i][0]=0
                    
        for i in range(1,m):
            if matrix[i][0]==0:
                for j in range(n):
                    matrix[i][j]=0

        for j in range(1,n):
            if matrix[0][j]==0:
                for i in range(m):
                    matrix[i][j]=0

        if row_zero==0:
            for j in range(n):
                matrix[0][j]=0
        if col_zero==0:
            for i in range(m):
                matrix[i][0]=0
                  