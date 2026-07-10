class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1 , max(piles)

        while left < right:
            mid = (left + right)//2

            print(left, right, mid)
            no_hours = sum(math.ceil(pile/mid) for pile in piles)
            print(no_hours)

            if no_hours <= h : 
                ## eating too fast can go slower
                right = mid
            else:
                left = mid+1

        return left


