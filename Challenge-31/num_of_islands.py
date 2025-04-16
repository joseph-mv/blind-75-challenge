class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        '''
        Find out number of islands which is surrounded by water and is formed by 
        connecting adjacent lands horizontally or vertically
        Args:
            An m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water).
        Return:
            Number of islands
        '''
        m=len(grid)
        n=len(grid[0])

        visited=[[False for _ in range(n)] for _ in range(m)]

        def dfs(r,c,visited):
            if r<0 or r>=m or c<0 or c>=n or visited[r][c] or grid[r][c]=='0':
                return 
            visited[r][c]=True

            dfs(r+1,c,visited)
            dfs(r-1,c,visited)
            dfs(r,c+1,visited)
            dfs(r,c-1,visited)

        num=0
        for r in range(m):
            for c in range(n):
                if not visited[r][c] and grid[r][c]=='1':
                    num+=1
                    dfs(r,c,visited)
        return num
        