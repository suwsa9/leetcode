class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasht = {}
        for i in range(len(nums)):
            want = target - nums[i]
            if want in hasht:
                return list(sorted([i, hasht[want]]))
            else:
                hasht[nums[i]] = i
            