class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            subtrahend = target - value
            if subtrahend in nums[index + 1:]:
                return [index, nums.index(subtrahend, index + 1)]

        return list()