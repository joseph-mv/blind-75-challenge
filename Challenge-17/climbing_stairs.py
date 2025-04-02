class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Findout how many distinct ways can you climb to the top,
        Each time either climb 1 or 2 steps
        
        Args:
            n: No of stairs
        Returns:
            The number of distinct ways to climb the stairs.
        """
        if n==0:
            return 0
        prev_ways=0
        curr_ways=1
        for i in range(0,n):
            temp=curr_ways
            curr_ways+=prev_ways
            prev_ways=temp
        return curr_ways

        