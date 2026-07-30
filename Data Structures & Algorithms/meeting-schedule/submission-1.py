"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        res = sorted(intervals, key = lambda x: (x.start, x.end))
        n = len(res)
        if not res:
            return True
        curr_start, curr_end = res[0].start, res[0].end
        i = 1
        for i in range(1, n):
            next_start = res[i].start

            if  next_start < curr_end:
                return False
            
            curr_start, curr_end = res[i].start, res[i].end
        
        return True
