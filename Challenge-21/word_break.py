class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        String can be segmented into a space-separated sequence of one or more dictionary words.
        Args:
            s: string to check
            wordDict: dictonary words array
        Return:
            True or False

        """

        word_set =set(wordDict)
        dp=[True]
        for i in range(0,len(s)):
            j=i
            ext=False
            while j>=0:
                word=s[j:i+1]
                if word in word_set and dp[j]:
                    ext=True
                    break
                j-=1
            dp.append(ext)
        return dp[-1]



        