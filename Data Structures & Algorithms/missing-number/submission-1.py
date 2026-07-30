class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        req_sum = (n+1) * (n)//2
        curr_sum = sum(nums)

        return req_sum - curr_sum

       