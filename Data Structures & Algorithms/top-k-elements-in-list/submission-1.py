class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        g = {}
        for i in nums:
         if i in g:
                g[i] += 1
         else: 
                g[i] = 1  
               
        topk = sorted(g.items(), key=lambda x: x[1], reverse = True) [:k]
        ans = []
        for num, freq in topk:
            ans.append(num)

        return ans    