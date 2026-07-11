class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        freq = {}

        for i in t:
            freq[i] = freq.get(i, 0) + 1

        window = {}
        have = 0
        freqcount = len(freq)

        res = [-1, -1]
        reslen = float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1   

            if c in freq and window[c] == freq[c]:
                have += 1
            while have == freqcount:
                if (r - l + 1) < reslen:
                    res = [l,r]
                    reslen = r - l + 1
                left = s[l]
                window[left] -= 1
                if left in freq and window[left ] < freq[left]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if reslen != float("inf") else ""                             

