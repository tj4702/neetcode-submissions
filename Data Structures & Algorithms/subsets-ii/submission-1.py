class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)
        nums.sort()

        def backtrack(curr, i):

            res.append(curr[:])

            for j in range(i,n):
                if nums[j-1] == nums[j] and j >i:
                    continue 
                
                curr.append(nums[j])
                backtrack(curr, j+1)
                curr.pop()

        
        backtrack([], 0)

        return res
        