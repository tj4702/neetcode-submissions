class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.append(newInterval)

        intervals = sorted(intervals, key = lambda interval: (interval[0], interval[1]))

        # print(intervals)

        res = []

        prev_start, prev_end = intervals[0][0], intervals[0][1]

        for start, end in intervals[1:]:

            if prev_start <= start <= prev_end:
                prev_end = max(prev_end, end)
                prev_start = min(start, prev_start)
            
            else:
                res.append([prev_start, prev_end])
                prev_start = start
                prev_end = end

            # print(res)

        
        res.append([prev_start, prev_end])
        # print(res)
        intervals = res

        return intervals
        