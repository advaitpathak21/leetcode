class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        result = 0
        l = 0
        r = 1
        
        while (r < n):
            if (prices[l] > prices[r]):
                l = r
                r += 1
            elif (prices[l] <= prices[r]):
                if (result < prices[r] - prices[l]):
                    result =A prices[r] - prices[l]
                r += 1
        return result
