class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slen = len(s)
        shash = {}
        thash = {}
        if slen != len(t): return False
        for i in range(slen):
            shash[s[i]] = shash.get(s[i], 0) + 1
            thash[t[i]] = thash.get(t[i], 0) + 1
        return shash == thash