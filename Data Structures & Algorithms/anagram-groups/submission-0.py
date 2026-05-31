class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        g = {}
        for word in strs:
            k = ''.join(sorted(word))

            if k not in g:
                g[k] = []

            g[k].append(word)

        return list(g.values())