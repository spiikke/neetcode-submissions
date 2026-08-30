class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        for i in range(1,len(prices)):
            current = prices[i] - prices[l]
            if current <= 0:
                l = i
            profit = max(current, profit)
        return profit


        