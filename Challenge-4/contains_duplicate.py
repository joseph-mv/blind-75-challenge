from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        if any value appears at least twice in the array, 
        and return false if every element is distinct
        """
        num_set=set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False