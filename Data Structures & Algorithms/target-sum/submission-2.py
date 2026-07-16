class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)

        if total < target:
            return 0 

        pos_sum = 0 

        if (target + total) % 2 == 1  :
            return 0 

        pos_target = (target + total)//2
        n = len(nums)
        res = 0 

        def backtrack(curr_sum, i):
            nonlocal res

            if i == n :
                if curr_sum == pos_target:
                    res+=1
                return 
            
            backtrack(curr_sum + nums[i], i+1)
            backtrack(curr_sum, i+1)
            
        
        backtrack(0, 0)

        return res

            
        