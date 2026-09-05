class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n <= 2 :
            return max(nums)

        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = nums[0] 

        for i in range(1, n):
            dp[i+1] = max(dp[i], dp[i-1]+nums[i])

        # print(dp)

        return dp[-1]



        