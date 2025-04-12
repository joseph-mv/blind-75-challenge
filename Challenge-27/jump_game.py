class Solution:
    def canJump(self, nums: list[int]) -> bool:
        '''
        FIndout is it possible to reach last index. You are initially positioned at the array's first index,
        and each element in the array represents your maximum jump length at that position.

        Args:
            nums:integer array num
        Return:
            True if you can reach the last index, or false otherwise.

        '''

        last_reach=nums[0]
        for i in range(1,len(nums)):
            if i>last_reach:
                return False
            last_reach=max(last_reach,i+nums[i])
        return True

        