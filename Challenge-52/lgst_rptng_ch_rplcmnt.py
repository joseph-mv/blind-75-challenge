class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring containing the same letter
        you can get after performing at most k operations.

        ARGS:
            s : The input string.
            k : The maximum number of changes allowed.

        Returns:
            int: The length of the longest substring with the same letter.
        """
        l= 0
        count={}
        max_freq=0
        max_len=0
        for  r in range(len(s)):
            count[s[r]] = count.get(s[r], 0)  +1
            max_freq=max(max_freq, count[s[r]])

            while r-l+1-max_freq > k:
                    count[s[l]] -=1
                    l+=1

            max_len=max(max_len, r-l+1)              
            r+=1

        return max_len