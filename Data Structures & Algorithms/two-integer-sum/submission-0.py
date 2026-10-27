class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nhash = {}
        for i in range(len(nums)):
            curr = nums[i]
            val = target - nums[i]
            if val in nhash:
                return [nhash.get(val), i]
            nhash[nums[i]] = i



        