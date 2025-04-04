class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        Calculate  the length of the longest strictly increasing subsequence.
        Args:
            A list of integers
        Returns:
            The length of the longest strictly increasing subsequence
        """

        sub_arr=[]

        for num in nums:
            if not sub_arr or sub_arr[-1]<num:
                sub_arr.append(num)
            else:
                left=0
                right=len(sub_arr)-1
                while left<right:
                    mid=(left+right)//2
                    if sub_arr[mid]<num:
                        left=mid+1
                    else:
                        right=mid
                sub_arr[left]=num
        return len(sub_arr)


        