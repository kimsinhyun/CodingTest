# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# sliding window

# my solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        profit = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            profit = max(profit, prices[r]-prices[l])
            
            r += 1
        return profit
    
# for loop instead of while loop because 
# r always incrementally increases by 1

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        p = 0
        for price in prices:
            if price < l:
                l = price
            if price - l > p:
                p = price - l
        return p