class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        res = []


        def backtrack(curr, curr_sum, i):
            if curr_sum == target:
                res.append(curr[:])
                return 

            if curr_sum > target or i >=n:
                return 

            for j in range(i,n):
                curr.append(nums[j])
                backtrack(curr, curr_sum + nums[j], j)
                curr.pop()

        backtrack([], 0,0)

        return res
