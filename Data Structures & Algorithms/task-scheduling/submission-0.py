class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        from collections import Counter

        count = Counter(tasks)
        maxFreq = max(count.values())
        numTasksWithMaxFreq = sum(1 for v in count.values() if v == maxFreq)

        c1 = (maxFreq - 1) * (n+1) + numTasksWithMaxFreq 
        c2 = len(tasks)

        return max(c1, c2)

        






        