class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        '''
        The word can be constructed from letters of sequentially adjacent cells,
        where adjacent cells are horizontally or vertically neighboring.
        The same letter cell may not be used more than once.

        Args:
            board: m x n grid of characters
            word: word for checking
        Returns:
            True if word exists in the grid, otherwise False.
        '''
        m ,n = len(board), len(board[0])

        def dfs(i, j, k):
            if k== len(word):
                return True

            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == "#" or board[i][j]!=word[k]:
                return False

            temp = board[i][j]
            board[i][j] = "#"

            found = (
                dfs(i + 1, j, k+1)
                or dfs(i - 1, j, k+1)
                or dfs(i, j + 1, k+1)
                or dfs(i, j - 1, k+1)
            )
            board[i][j] = temp
            return found

        for i in range(m):
            for j in range(n):
                exist = dfs(i, j, 0)
                if exist:
                    return True

        return False  
