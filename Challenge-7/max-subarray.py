from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find the subarray with the largest sum, and return its sum.
        """
        sum=0
        max_sum=float('-inf')
        for num in nums:
            total=sum+num
            sum=max(total,num)
            max_sum=max(max_sum,sum)
        return max_sum
       

        