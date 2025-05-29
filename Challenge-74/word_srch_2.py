class TrieNode:
    def __init__(self):
        self.children={}
        self.isWord=False
    def addword(self,word):
        root = self
        for ch in word:
            if ch not in root.children:
                root.children[ch]=TrieNode()
            root=root.children[ch]
        root.isWord= True

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Findout all words on the board
        Args:
            board : 2D board of characters
            words : List of words to search in the board

        Returns:
            List of all words found in the board
        """
        root = TrieNode()
        for w in words:
            root.addword(w)
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        def dfs(r, c, node, word):
            if (r<0 or r == ROWS or c<0 or c== COLS or (r,c) in visit or board[r][c]  not in node.children):
                return
            visit.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.isWord:
                res.add(word)
            dfs(r,c+1,node,word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)


            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root,'')
        return list(res)
        