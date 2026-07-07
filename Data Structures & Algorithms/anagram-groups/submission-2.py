class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        strs2 = [''.join(sorted(s)) for s in strs]
        n = len(strs)

        for i in range(n):
            res[strs2[i]].append(strs[i])
        
        final = [v for v in res.values()]

        return final
