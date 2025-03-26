from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Given the array nums after the possible rotation and an integer target, 
        return the index of target if it is in nums, or -1 if it is not in nums.
        """
        left,right= 0,len(nums)-1

        while left<=right:
            mid=(left+right)//2
            mid_num=nums[mid]
            if mid_num==target:
                return mid

            if mid_num>nums[right]:
                if target>=mid_num or target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1

            else:
                if target<mid_num or target>nums[right]:
                    right=mid-1
                else:
                    left=mid+1
        return -1
      
            
            