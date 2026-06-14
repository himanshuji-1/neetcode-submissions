class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      l = 0
      res = 0
      w = set()
      for i in range(len(s)):
        while s[i] in w:
            w.remove(s[l])
            l += 1
        w.add(s[i])
        res = max(res, i - l + 1)
      return res  
