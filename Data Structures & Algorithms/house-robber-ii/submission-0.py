class Solution:
    def rob(self, nums: List[int]) -> int:


        def rob_linear(nums):
            n = len(nums)

            if n ==1:
                return nums[0]
            if n == 0 :
                return 0 

            dp = [0] * (n+1)
            dp[1] = nums[0]

            for i in range(1, n):
                dp[i+1] = max(nums[i] + dp[i-1], dp[i])

            # print(dp)
            return dp[-1]
        
        n = len(nums)

        if n == 0:
            return 0
        
        if n ==1:
            return nums[0]

        option1 = rob_linear(nums[1:])
        option2 = rob_linear(nums[0:-1])

        return max(option1, option2)


        