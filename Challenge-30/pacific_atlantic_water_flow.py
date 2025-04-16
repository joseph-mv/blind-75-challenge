class Solution:
    '''
    Finds all the cells in a rectangular island from which rainwater can 
    flow to both the Pacific and Atlantic oceans.

        The Pacific Ocean touches the island's left and top edges.
        The Atlantic Ocean touches the island's right and bottom edges.
        Water can flow from a cell to its neighbors (north, south, east, west) 
        if the neighbor's height is less than or equal to the current cell's height.
        Water can flow from any cell adjacent to an ocean into that ocean.

    Args:
        heights: An m x n integer matrix where heights[r][c] represents the height 
        of the cell at coordinate (r, c).

    Returns:
        A 2D list of grid coordinates [[ri, ci]] where rainwater can flow from cell 
        (ri, ci) to both oceans.
        

    '''
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m=len(heights)
        n=len(heights[0])

        pacific_reachable=[[False for _ in range(n)] for _ in range(m)]
        atlantic_reachable=[[False for _ in range(n)] for _ in range(m)]

        def dfs(r,c,reachable,prev_height):
            if r<0 or r>=m or c<0 or c>=n or reachable[r][c] or heights[r][c]<prev_height:
                return
            reachable[r][c]=True

            dfs(r-1,c,reachable,heights[r][c])
            dfs(r+1,c,reachable,heights[r][c])
            dfs(r,c-1,reachable,heights[r][c])
            dfs(r,c+1,reachable,heights[r][c])


        for r in range(m):
            dfs(r,0,pacific_reachable,-1)

        for c in range(n):
            dfs(0,c,pacific_reachable,-1)

        for r in range(m):
            dfs(r,n-1,atlantic_reachable,-1)

        for c in range(n):
            dfs(m-1,c,atlantic_reachable,-1)

        
        result=[]
        for r in range(m):
            for c in range(n):
                if atlantic_reachable[r][c] and pacific_reachable[r][c]:
                    result.append([r,c])


        return result