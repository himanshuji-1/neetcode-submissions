class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      map = {}
      res = 0
      l = 0

      for i in range(len(s)):
        map[s[i]] = 1 + map.get(s[i], 0)

        while (i - l + 1) - max(map.values()) > k:
          map[s[l]] -= 1
          l += 1
        res = max(res, i - l + 1 )
      return res  