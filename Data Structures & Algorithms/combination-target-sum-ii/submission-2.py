class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        candidates.sort()
        n = len(candidates)
        currSum = 0 
        res = []

        def backtrack(curr_path, curr_sum, i):

            if curr_sum == target:
                res.append(curr_path[:])
                return 

            if i >= n  or curr_sum > target:
                return 

            for j in range(i, n):
                if candidates[j] == candidates[j-1] and j > i:
                    continue
                
                if curr_sum + candidates[j] > target:
                    break
                curr_path.append(candidates[j])
                backtrack(curr_path, curr_sum + candidates[j], j+1)
                curr_path.pop()

        backtrack([], 0, 0)

        return res


