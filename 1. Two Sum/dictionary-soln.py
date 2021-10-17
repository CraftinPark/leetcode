class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = dict()
        for i in range(len(nums)):
            if nums[i] in complementMap:
                return [complementMap[nums[i]], i]
            else:
                complementMap[target - nums[i]] = i;