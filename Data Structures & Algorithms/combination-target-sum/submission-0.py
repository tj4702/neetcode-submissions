class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        n= len(nums)
        
        def backtrack(curr_path, curr_sum, i):

            if curr_sum == target:
                res.append(curr_path[:])
                return 
            
            if curr_sum > target or i >= n:
                return 
            

            for j in range(i, n):
                curr_path.append(nums[j])
                backtrack(curr_path, curr_sum+nums[j], j)
                curr_path.pop()

        
        backtrack([], 0, 0)

        return res

