class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        req_sum = sum(x for x in range(n+1))
        curr_sum = sum(x for x in nums)

        # print(req_sum)
        # print(curr_sum)

        return req_sum - curr_sum

       