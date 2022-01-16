class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > curr:
                res += (prices[i] - prices[i - 1])
            curr = prices[i]
        return res