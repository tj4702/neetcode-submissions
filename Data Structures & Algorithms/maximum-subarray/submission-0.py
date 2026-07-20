class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = nums[0]
        n = len(nums)


        def backtrack(currSum, i):
            nonlocal maxSum

            if i == n :
                return 
            
            currSum = max(currSum + nums[i],nums[i])
            
            maxSum = max(maxSum, currSum)
            
        
            backtrack(currSum, i + 1)

        
        backtrack(nums[0],1)
        return maxSum

        