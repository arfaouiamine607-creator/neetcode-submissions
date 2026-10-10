class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        b = {}
        d = {}

        for i in range(0,len(s)):
            b[s[i]] = b.get(s[i],0) + 1
            d[t[i]] = d.get(t[i],0) + 1
        
        return b == d