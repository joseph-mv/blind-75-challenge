class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Findout number of palindromic substirngs in given string.
        Args:
            s:Input string
        Returns:
            Number of palindromic substrings.
        '''
        n = len(s)
        count = 0

        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count
