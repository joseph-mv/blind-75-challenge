from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Find minimum window substring of s such that every character in t (including duplicates) is included in the window. 
        Args:
            s: Input string
            t: The string containing the characters that must be included in the window.
        Returns:
            Minimum window substring of s.If there is no such substring, return the empty string "".
        '''
        t_dict = defaultdict(int)
        s_dict = defaultdict(int)
        
        for ch in t:
            t_dict[ch] += 1
            s_dict[ch] = 0
        need, have = len(t), 0

        l=0
        substr=''
        min_len=float('inf')
        for r, ch in enumerate(s):
            if ch in t_dict:
                s_dict[ch] += 1
                if s_dict[ch] <= t_dict[ch]:
                    have += 1

            while have == need:
                if min_len > r-l+1:
                    min_len = r-l+1
                    substr = s[l:r+1]
                
                if s[l] in t_dict:
                    s_dict[s[l]] -= 1
                    if s_dict[ s[l] ] < t_dict[ s[l] ]:
                        have -= 1
                l += 1
        return substr

        