class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        res  = []


        intervals = sorted(intervals, key = lambda interval: (interval[0], interval[1]))

        prev_start, prev_end = intervals[0][0], intervals[0][1]

        for start, end in intervals[1:]:

            if prev_start <= start <= prev_end:
                prev_end = max(prev_end, end)

            else:
                res.append([prev_start, prev_end])
                prev_start, prev_end = start, end

        
        res.append([prev_start, prev_end])

        return res
        