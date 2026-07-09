class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        freq1 = {}
        for ch in s1:
            freq1[ch] = freq1.get(ch, 0) + 1

        freq2 = {}
        for i in range(len(s1)):
            freq2[s2[i]] = freq2.get(s2[i], 0) + 1

        if freq1 == freq2:
            return True

        for i in range(len(s2) - len(s1)):
            left = s2[i]
            freq2[left] -= 1

            if freq2[left] == 0:
                del freq2[left]

            right = s2[i + len(s1)]
            freq2[right] = freq2.get(right, 0) + 1

            if freq1 == freq2:
                return True

        return False