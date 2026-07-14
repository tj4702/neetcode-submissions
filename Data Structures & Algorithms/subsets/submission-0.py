class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []


        def backtrack(curr_path, i):
            if i == n :
                res.append(curr_path[:])
                return 
            
            backtrack(curr_path + [nums[i]], i+1)
            backtrack(curr_path, i+1)

        
        backtrack([], 0)

        return res


        