"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key= lambda x: (x.start, x.end))

        if not intervals:
            return True

        start, end = intervals[0].start, intervals[0].end
        n = len(intervals)

        for i in range(1,n):
            curr_start, curr_end = intervals[i].start, intervals[i].end

            if curr_start < end :
                return False
            start, end = curr_start, curr_end

        return True
