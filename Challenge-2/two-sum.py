from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices 
        of the two numbers such that they add up to target.
        """
        hash={}
        for idx in range(0 ,len(nums)):
            complement=target-nums[idx]
            if complement in hash:
                return [idx,hash[complement]]
            hash[nums[idx]]=idx