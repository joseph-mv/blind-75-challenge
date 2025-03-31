class Solution:
    def missingNumber(self, nums: list[int]) -> int:   
        """
        Finds missing number in the range [0,n] from array.
        Args:
            nums:A list of distinct numbers in the range [0,n]
        Returns:
            The missing number.
        """     

        ls_num=len(nums)
        n_sum=ls_num*(ls_num+1)/2

        num_sum=0
        for num in nums:
            num_sum+=num

        return int(n_sum-num_sum)