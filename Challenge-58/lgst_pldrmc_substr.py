class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Findout longest Palindromic substring
        Args:
            s: Input string
        Returns:
            longest substring
        '''
        left , right, n = 0, 0, len(s)
        
        for i in range(n):
            l = r = i
            while l>=0 and r < n and s[l] == s[r]:
                if r-l > right- left:
                    left = l
                    right = r
                l -= 1
                r += 1

            l , r = i, i+1
            while l>=0 and r < n and s[l] == s[r]:
                if r-l > right- left:
                    left = l
                    right = r
                l -= 1
                r += 1
        return s[left:right+1]

        