class Solution:
    def countBits(self, n: int) -> list[int]:
        """
        Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
        result[i] is the number of 1's in the binary representation of i
        """
        result=[0]
        for num in range(1,n+1):
            bits_count= result[ num//2 ] + num % 2
            result.append(bits_count)
        return result