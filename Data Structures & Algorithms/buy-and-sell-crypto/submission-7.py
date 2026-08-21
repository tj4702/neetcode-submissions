class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minBuy = prices[0]
        res = 0 
        n = len(prices)

        for sell in prices:
            res = max(res, sell - minBuy)
            minBuy = min(minBuy, sell)

        return res


        