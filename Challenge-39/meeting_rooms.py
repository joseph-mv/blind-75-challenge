
# Definition of Interval:

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        '''
        Determine if a person could add all meetings to their 
        schedule without any conflicts.
        Args:
            intervals:An array of meeting time interval objects 
            consisting of start and end times.
        Returns:
            True if all meetings can be attended without conflict, 
            False otherwise.
        '''
        if not intervals:
            return True

        arr=[]
        for interval in intervals:
            arr.append([interval.start, interval.end])
        arr.sort()

        prevEnd=arr[0][1]
        for interval in arr[1:]:
            if interval[0]<prevEnd:
                return False
            else:
                prevEnd=interval[1]

        return True