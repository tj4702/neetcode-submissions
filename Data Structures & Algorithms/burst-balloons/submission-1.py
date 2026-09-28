class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        n = len(nums)
        padded = nums

        memo = {}

        def dfs(left, right):

            if (left, right) in memo:
                return memo[(left, right)]

            if left + 1 == right:
                return 0 

            best = 0 

            for k in range(left+1, right):
                coins = padded[left] * padded[k] * padded[right]
                coins += dfs(left,k) + dfs(k, right)
                best = max(best , coins)
                memo[(left, right)] = best
            return best

        return dfs(0,n-1)


        