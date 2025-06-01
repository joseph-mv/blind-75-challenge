class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Find the k most frequent elements.
        Args:
            nums: List of integers
            k: Number of top frequent elements to return

        Returns:
            List of k most frequent elements
        """

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        freq = [[] for _ in range(len(nums)+1)]

        for key, val in count.items():
            freq[val].append(key)
        lst = [item for sublist in freq for item in sublist]
        
        return lst[-k:]
        