class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        '''
        Group Anagrams
            An anagram is a word or phrase formed by rearranging the letters of a 
            different word or phrase, using all the original letters exactly once.
        Args: 
            strs: List of input strings
        Returns:
            list of groups of anagrams.
        '''
        
        obj={}
        for string in strs:
            sort_str =  ''.join(sorted(string))
            if sort_str not in obj:
                obj[sort_str] = []
            obj[sort_str].append(string)

        return list(obj.values())
                
        
