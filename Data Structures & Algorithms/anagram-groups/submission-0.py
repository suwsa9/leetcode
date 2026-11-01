class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # iterate thru, sorted is key, val is array
        hasht = {}
        for s in strs:
            k = "".join(sorted(s))
            if k in hasht:
                hasht[k].append(s)
            else:
                hasht[k] = [s]
        
        return list(hasht.values())
