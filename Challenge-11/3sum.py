class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
        such that i != j,      i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        
        Notice that the solution set must not contain duplicate triplets.
        """
        nums.sort()
        result=[]
        i=0
        right=len(nums)-1
        while i < right:
            num=nums[i]
            j=i+1
            k=right
            while j<k:
                total=num+nums[j]+nums[k]
                if total==0:
                    result.append([num,nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1] :
                        j=j+1
                    while j<k and nums[k]==nums[k-1]:
                        k=k-1
                    j=j+1
                    k=k-1
                elif total<0:
                    j=j+1
                else:
                    k=k-1
            while i<right and num==nums[i+1]:
                i=i+1
            i=i+1



        return result



