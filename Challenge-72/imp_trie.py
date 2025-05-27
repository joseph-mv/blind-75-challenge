class Trie:

    def __init__(self):
        self.obj = {}

    def insert(self, word: str) -> None:
        '''
        Insert a word into trie
        Args:
            word: Input word
        '''
        obj = self.obj
        for ch in word:

            if ch not in obj:
                obj[ch] = {}
            obj = obj[ch]
        obj["#"] = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word exists in the trie.
        Args:
            word: The word to search.
        Returns:
            True if word is found, False otherwise.
        """
        obj = self.obj
        for ch in word:
            if ch not in obj:
                return False
            obj = obj[ch]
        return obj.get("#", False)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts
         with the given prefix.
        Args:
            prefix : The prefix to check.
        Returns:
            True if a word with given prefix exists, False otherwise.
        """
        obj = self.obj
        for ch in prefix:
            if ch not in obj:
                return False
            obj = obj[ch]
        return True    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
