class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasht = {}
        for i, n in enumerate(nums):
            want = target - n
            if want in hasht:
                return [hasht[want], i]
            hasht[n] = i
            