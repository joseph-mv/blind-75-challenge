class WordDictionary:

    def __init__(self):
        self.dic={}
        
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        
        Args:
            word: The word to be added.
        """
        dic=self.dic
        for ch in word:
            if ch not in dic:
                dic[ch] = {}
            dic = dic[ch]
        dic['#'] = True

    def search(self, word: str) -> bool:
        """
        Searches for a word or pattern with '.' as wildcard.
        
        Args:
            word (str): The word or pattern to search.
        
        Returns:
            True if any word in the structure matches the pattern,
            False otherwise.
        """
        def dfs(i, obj):
            if i>=len(word):
                return obj.get('#',False)

            if word[i] == '.':
                for ch in obj:
                    if(dfs(i+1, obj[ch])):
                        return True
                return False
                
            if  word[i] not in obj:
                return False
            return dfs(i+1,obj[word[i]])
        return dfs(0,self.dic)

        
   

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)