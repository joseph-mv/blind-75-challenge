class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        return number of set bits in its binary representation 
        """
        count=0
        while n:
            count+=n&1
            n>>=1
        return count