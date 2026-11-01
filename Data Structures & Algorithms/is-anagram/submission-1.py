class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return "".join(sorted(s, key=str)) == "".join(sorted(t, key=str))