class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s)-1
        for i, n in enumerate(s):
            if not n.isalnum():
                continue
            if i > j:
                return True
            while not s[j].isalnum():
                j -= 1
            if s[j].lower() != n.lower():
                return False
            j -= 1
        return True

        