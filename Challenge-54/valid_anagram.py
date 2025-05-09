class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Valid anagram
            An anagram is a word or phrase formed by rearranging the letters of a different 
            word or phrase, using all the original letters exactly once.
        Args:
            s: Input string
            t: Second Input string
        Returns:
            True if t is an anagram of s, and False otherwise.
        '''
        if len(s) != len(t):
            return False
        
        s_obj = {}
        t_obj = {}
        for char1, char2 in zip(s, t):
            s_obj[char1] = s_obj.get(char1, 0) +1
            t_obj[char2] = t_obj.get(char2, 0) +1
        
        for ch in s_obj:
            if s_obj[ch] != t_obj.get(ch):
                return False

        return True
