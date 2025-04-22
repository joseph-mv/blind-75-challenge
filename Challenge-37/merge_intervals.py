class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        '''
        Merge intervals
        Args:
            intervals:Array of intervals where intervals[i] = [starti, endi]
        Returns:
            An array of the non-overlapping intervals that cover all the intervals in the input.
        '''

        sorted_intervals=sorted(intervals)
        result=[]

        for interval in sorted_intervals:
            if not result or result[-1][1]<interval[0] :
                result.append(interval)
            else:
                result[-1][1]=max(interval[1],result[-1][1])

        return result