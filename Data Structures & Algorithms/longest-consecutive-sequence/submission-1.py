class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = sorted(set(nums))
        n = len(nums)
        res = [1] * n

        for i in range(1,n):
            if nums[i] - nums[i-1] == 1:
                res[i] += res[i-1]
        
        return max(res) if res else 0

        