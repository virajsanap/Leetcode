class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        first = prices[0]
        for i in range(1, len(prices)):
            if (first>prices[i]):
                first = prices[i]
            else:
                maxProfit += prices[i]-first
                first = prices[i]
        return maxProfit