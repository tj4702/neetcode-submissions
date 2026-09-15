class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        if n == 0 :
            return 0 

        buy = [0] * n 
        buy[0] = -prices[0]

        avl_cash = [0] * n 

        for i in range(1,n):
            buy[i] = max(buy[i-1], avl_cash[i-2]- prices[i])
            avl_cash[i] = max(avl_cash[i-1], buy[i-1] + prices[i])

        return max(buy[-1], avl_cash[-1])
