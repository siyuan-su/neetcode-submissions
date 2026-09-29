class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mprofit = 0

        if len(prices) == 2:
            if prices[1] > prices[0]:
                return prices[1] - prices[0]
            else:
                return 0

        for i in range(1, len(prices)):
            for j in range(i):
                profit = prices[i] - prices[j]
                if profit > mprofit:
                    mprofit = profit
        
        if mprofit < 0:
            return 0

        return mprofit