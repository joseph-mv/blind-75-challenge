class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        longest common subsequence. 

        A subsequence of a string is a new string generated from the original string 
        with some characters (can be none) deleted without changing the relative order of the remaining characters.
        
        Args:
            Two strings
        Return:
            Length of longest common subsequence
        """

        m=len(text1)
        n=len(text2)
        matrix = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(0,m):
            for j in range(0,n):
                if text1[i]==text2[j] :                   
                    if i>0 and j>0:
                        matrix[i][j]=max(matrix[i-1][j-1]+1,matrix[i-1][j],matrix[i][j-1])
                    else:
                        matrix[i][j]=1
                else:
                    matrix[i][j]=max(matrix[i-1][j],matrix[i][j-1])
        
        return matrix[m-1][n-1]
                        
        
        
        

        





        