class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        res = 0

        for i in range(len(prices)):
            for j in range(i):
             
                p = prices[i] - prices[j]
                res = max(res, p)
              
        return res        

        