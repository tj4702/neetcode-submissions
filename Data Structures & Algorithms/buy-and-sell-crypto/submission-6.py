class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        prev_day = 0 
        res =0 
        n = len(prices)

        for i in range(1, n):
            if prices[i] > prices[prev_day]:
                res = max(res,  prices[i] - prices[prev_day] )
            else:
                prev_day = i

        return res


        