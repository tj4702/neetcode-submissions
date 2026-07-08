class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total_sum = sum(nums)

        if total_sum % 2 !=0 :
            return False
        
        n = len(nums)
        target = total_sum // 2
        curr_sum = 0 

        def check(i, curr_sum):
            
            if curr_sum == target:
                return True
            
            if i == n :
                return False
            
            return check(i+1, curr_sum + nums[i]) or check(i+1, curr_sum)

        return check(0, 0)

            
