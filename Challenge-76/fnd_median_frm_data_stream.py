import heapq


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        """
        Adds a number into the heap.

        """
        max_h = self.max_heap
        min_h = self.min_heap
        heapq.heappush(max_h, -num)

        if len(max_h) - len(min_h) > 1:
            num = -heapq.heappop(max_h)
            heapq.heappush(min_h, num)

        if max_h and min_h and -max_h[0] > min_h[0]:
            num = -heapq.heappop(max_h)
            heapq.heappush(min_h, num)
        if len(min_h) - len(max_h) > 1:
            num = heapq.heappop(min_h)
            heapq.heappush(max_h, -num)

    def findMedian(self) -> float:
        """
        Returns the median of current data stream.
        """
        len_min = len(self.min_heap)
        len_max = len(self.max_heap)
        if len_min == len_max:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        if len_min > len_max:
            return self.min_heap[0]
        return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
