class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        res = []

        def dfs(curr_path, i):

            res.append(curr_path[:])
            
            for j in range(i,n):
                if j > i and nums[j] == nums[j-1] :
                    continue
                
                curr_path.append(nums[j])
                dfs(curr_path, j+1)
                curr_path.pop()

        
        dfs([], 0)

        return res

        