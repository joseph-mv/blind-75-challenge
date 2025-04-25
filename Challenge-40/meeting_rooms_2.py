"""
Definition of Interval:
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        '''
        Find the minimum number of days required to schedule all meetings
        without any conflicts. A day can hold multiple meetings as long as 
        their times do not overlap.

        Args:
            intervals: An array of meeting time interval objects 
            consisting of start and end times [start_i, end_i].

        Returns:
            Minimum number of days required to accommodate all meetings 
            without any overlap in a single day.
        '''
        if not intervals:
            return 0

        start=[]
        end=[]
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()

        count=0
        max_count=0
        i,j=0,0
        while i<len(start) and j<len(end):

            if start[i]<end[j]:
                count+=1
                i+=1
            else:
                j+=1
                count-=1
            max_count=max(max_count,count)
        return max_count
