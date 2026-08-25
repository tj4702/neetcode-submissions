class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        n = len(candidates)
        res = []

        def backtrack(curr, curr_sum, i):
            if curr_sum == target:
                res.append(curr[:])
                return 
            
            if curr_sum > target or i >=n:
                return 

            for j in range(i, n):
                if candidates[j-1] == candidates[j] and j > i:
                    continue
                if curr_sum + candidates[j] > target:
                    break
                curr.append(candidates[j])
                backtrack(curr, curr_sum + candidates[j], j+1)
                curr.pop()

        backtrack([],0,0)

        return res

        
        