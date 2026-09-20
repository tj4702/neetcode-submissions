class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m, n = len(nums1), len(nums2)
        tot = m+n 
        left_half = (tot+1)//2

        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        lo, hi = 0, m 

        while lo <= hi:
            i  = (lo+hi)//2
            j = left_half - i 

            left1 = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j-1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                if tot % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                hi = i - 1

            else:
                lo = i+1





