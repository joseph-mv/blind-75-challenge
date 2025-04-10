class Solution:
    """
    Calculate the maximum amount of money can rob tonight without 
    alerting the police from circular arranged houses.

    Args:
        nums: A list of integers representing the amount of money in each house.

    Returns:
        The maximum amount of money the robber can steal.
    """
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        def rob_linear( nums: list[int]) -> int:
            n=len(nums)
            if n==1:
                return nums[0]

            prev2=nums[0]
            prev1=max(nums[0],nums[1])

            for i in range(2,n):
                curr=max(prev1,prev2+nums[i])
                prev2=prev1
                prev1=curr               
            return prev1

        return max(rob_linear(nums[0:-1]) , rob_linear(nums[1:]))
