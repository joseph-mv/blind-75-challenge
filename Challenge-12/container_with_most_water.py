class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        You are given an integer array height of length n. 
        each element in array represent height of line.
        Find two lines that together with the x-axis form a container, such that the container contains the most water.
        Return the maximum amount of water a container can store.
        """

        left=0
        right=len(height)-1
        max_wtr=0
        while left<right:
            amt_wtr=(right-left)*min(height[left],height[right])
            max_wtr=max(max_wtr,amt_wtr)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_wtr

        