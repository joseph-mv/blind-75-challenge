class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        Find out the length of the longest consecutive elements sequence.
        Args:
            nums:Unsorted array of integers
        Return:
            Length of longest consecutive sequence
        """
        num_set = set(nums)
        long_con_seq = 0
        for num in num_set:
            if num - 1 not in num_set:
                curr_seq = 0
                while num in num_set:
                    curr_seq += 1
                    num += 1
                long_con_seq = max(long_con_seq, curr_seq)
        return long_con_seq
