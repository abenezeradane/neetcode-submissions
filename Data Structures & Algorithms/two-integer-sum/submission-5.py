class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            minuend = target - value
            if minuend in nums:
                for itr, num in enumerate(nums):
                    if num == minuend and itr != index:
                        return [index, itr]
        return []