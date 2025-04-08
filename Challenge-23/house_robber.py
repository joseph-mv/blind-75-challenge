class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum amount of money that can be robbed without alerting the police.

        Args:
            nums: A list of the amount of money in each house.

        Returns:
            The maximum amount.
        """
         
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        prev2 = nums[0]         
        prev1 = max(nums[0], nums[1]) 

        for i in range(2, n):
            curr = max(nums[i] + prev2, prev1)  
            prev2 = prev1
            prev1 = curr

        return prev1
