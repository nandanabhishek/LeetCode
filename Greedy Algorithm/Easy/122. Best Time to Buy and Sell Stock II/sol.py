class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro = 0
        if not prices:
            return 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                maxpro += prices[i+1]-prices[i]
        return maxpro
        
