class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []
        for s in strs:
            sizes.append(str(len(s)))
            sizes.append('#')
            sizes.append(s)
        return "".join(sizes)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            i = j + 1
            j = i + l
            res.append(s[i:j])
            i = j
        
        return res   



