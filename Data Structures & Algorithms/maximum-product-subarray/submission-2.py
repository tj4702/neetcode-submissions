class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        dp_max = [num for num in nums] 
        dp_min = [num for num in nums]


        for i in range(1,n):
            dp_max[i] = max(dp_max[i-1] * nums[i], dp_max[i], dp_min[i-1] * nums[i])
            dp_min[i] = min(dp_min[i-1] * nums[i], dp_min[i], dp_max[i-1] * nums[i])


        return max(dp_max)


        