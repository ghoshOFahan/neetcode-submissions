class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current = prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>current:
                profit=max(profit,prices[i]-current)
            current=min(current,prices[i])
        return profit