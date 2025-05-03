class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        '''
        Return all elements of a matrix in spiral order.

        Args:
            matrix : 2D matrix of m x n integers.

        Returns:
            List: Elements in spiral traversal order.
        '''
        top, left=0, 0
        bottom, right=len(matrix), len(matrix[0])
        result=[]
        while True:
            if left==right:
                break
            # right direction
            for j in range(left, right):
                result.append( matrix[top][j] )
            top+=1

            if top==bottom:
                break
            # downward direction
            for i in range(top,bottom):
                result.append( matrix[i][right-1])
            right-=1

            if left==right:
                break
            # left direction
            for j in range (right-1, left-1, -1):
                result.append( matrix[bottom-1][j] )
            bottom-=1

            if bottom==top:
                break
            # upward direction
            for i in range(bottom-1, top-1, -1):
                result.append( matrix[i][left])
            left+=1

        return result
