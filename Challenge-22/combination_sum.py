class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        """
        Combination Sum
        find out number of possible combinations that add up to target

        Args:
            nums:array of distinct integers
            target: target integer
        Returns:
            number of possible combinations
        """

        dp=[1]
        for i in range (1,target+1):
            combo=0
            for num in nums:
                if num<=i:
                    combo+=dp[i-num]
            dp.append(combo)
        return dp[-1]

        