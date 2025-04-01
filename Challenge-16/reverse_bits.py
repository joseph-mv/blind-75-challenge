class Solution:
    def reverseBits(self, n: int) -> int:
        """
            Reverse bits of a given 32 bits unsigned integer.
        Args:
            n: The 32-bit unsigned integer.

        Returns:
            The reversed 32-bit unsigned integer.
        """
        rev_n = 0
        for i in range(32):
            last_bit = n & 1
            rev_n <<= 1
            rev_n |= last_bit
            n >>= 1

        return rev_n