class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Rotates the given n x n matrix by 90 degrees clockwise in place.
        Args:
            matrix: n*n 2D matrix
            
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i,n-1-i):               
                row=i
                col=j
                pass_value=matrix[i][j]
                for k in range(4):
                    row, col = col, n-1-row
                    matrix[row][col], pass_value = pass_value, matrix[row][col]
                    




        
        



        
            
