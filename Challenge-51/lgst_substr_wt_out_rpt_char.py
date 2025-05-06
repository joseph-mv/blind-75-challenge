class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Findout Longest substring without repeating characters.
        Args:
            s: The input string.
        Returns:
            Length of longest substring.
        '''
        string=''
        max_len=0

        for i in range(len(s)):

            while s[i] in string:
                string=string[1:]

            string += s[i]
            max_len=max(max_len, len(string))
        return max_len
            
                
        