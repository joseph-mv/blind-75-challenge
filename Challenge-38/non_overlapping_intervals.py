class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        '''
        Find minimum number of intervals need to remove to make the rest of the intervals non-overlapping.
        Args:
            intervals:An array of intervals where intervals[i] = [starti, endi]
        Returns:
            Minimum number of intervals    
        '''
        intervals.sort()
        res=0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start>=prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res