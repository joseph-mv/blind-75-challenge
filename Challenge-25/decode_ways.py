class Solution:
    """
    Calculates the number of ways to decode a string of digits.

    Args:
        s: The string of digits.

    Returns:
        The number of ways to decode the string.
    """
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        prev2=1
        prev1=1

        for i in range(1,len(s)):
            curr=0
            if int(s[i])>0:
                curr+=prev1
            if s[i-1]!='0' and int(s[i-1:i+1])<=26:
                curr+=prev2
            prev2=prev1
            prev1=curr
        return prev1

        