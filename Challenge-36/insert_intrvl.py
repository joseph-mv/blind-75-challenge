class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        """
        Inserts a new interval into a list of non-overlapping, sorted intervals
        and merges any overlapping intervals to maintain the non-overlapping property.

        Args:
            intervals: A list of non-overlapping intervals sorted by start time.
            newInterval: A new interval to insert and merge if necessary.

        Returns:
            A new list of merged intervals after insertion.
        """
        len_intervals=len(intervals)
        if not len_intervals:
            return [newInterval]

        idx=0
        ans=[]

        while idx<len_intervals and intervals[idx][0]<newInterval[0]:
            ans.append(intervals[idx])
            idx+=1
            
        if not len(ans) or ans[-1][1]<newInterval[0]:
            ans.append(newInterval)
        else:
            ans[-1][1]=max(ans[-1][1],newInterval[1])

        while idx<len_intervals:
            
            if ans[-1][1]<intervals[idx][0]:
                ans.append(intervals[idx])
            else:
                ans[-1][1]=max(ans[-1][1],intervals[idx][1])
            idx+=1


        return ans
           

        