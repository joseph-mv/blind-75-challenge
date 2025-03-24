from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find a subarray that has the largest product, 
        and return the product.
        """
        curr_min=1
        curr_max=1
        max_value=float('-inf')
        for num in nums:
            product1=curr_min*num
            product2=curr_max*num

            curr_min=min(num,product1,product2)
            curr_max=max(num,product1,product2)

            max_value=max(max_value,curr_max)
        return max_value
