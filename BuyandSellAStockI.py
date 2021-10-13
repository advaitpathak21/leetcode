class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        result = 0
        l = 0
        r = 1
        
        while (r < n):
            if (prices[l] >= prices[r]):
                l = r
            elif (prices[l] < prices[r]):
                profit = prices[r] - prices[l]
                result = max(result, profit)
            r += 1
        return result
