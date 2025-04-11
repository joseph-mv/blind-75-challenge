class Solution:
    '''
    Calculate number of of possible unique paths that the robot can take to reach the bottom-right corner.
    The robot can only move either down or right at any point in time.

    Args:
        Given the two integers m and n
    Return:
        The number of possible unique paths 
    '''
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j]=matrix[i][j-1]+matrix[i-1][j]
        return matrix[m-1][n-1]