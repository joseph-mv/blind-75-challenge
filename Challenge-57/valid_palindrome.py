import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Determines if a given string is a palindrome after converting all uppercase letters 
        into lowercase letters and removing all non-alphanumeric characters,.

        Args:
            s: The input string.

        Returns:
            True if the string is a palindrome, False otherwise.
        """
        s=s.lower()
        s=re.sub(r'[^a-z0-9]', '', s)
        return s==s[::-1]
        