class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        profit = 0
        for price in prices:
            curr = price - minp
            profit = max(curr, profit)
            if minp > price:
                minp = price
        return profit
    
#         l = 0
#         r = 1
#         res = 0
        
#         while r < len(prices):
#             if prices[l] >= prices[r]:
#                 l = r
#             res = max(res, prices[r] - prices[l])
#             r += 1
            
#         return (res)
        