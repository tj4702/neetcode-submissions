class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = defaultdict(int)

        for n in nums:
            counter[n] +=1


        res = [k for k,v in sorted(counter.items(), key = lambda item : -item[1])]


        return res[:k]
