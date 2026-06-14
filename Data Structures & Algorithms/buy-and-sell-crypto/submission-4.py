class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minpr = prices[0]
        maxp = 0
        for price in prices:
            minpr = min(minpr, price)

            p = price - minpr
            maxp = max(p, maxp)
        return maxp   