class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)

        def dfs(curr,i):
            if i == n:
                res.append(curr[:])
                return 

            dfs(curr+[nums[i]], i+1)
            dfs(curr, i+1)

        dfs([], 0 )

        return res
        