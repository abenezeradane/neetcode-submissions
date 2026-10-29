class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: Dict = dict()
        for index, value in enumerate(nums):
            subtrahend = target - value
            if subtrahend in seen:
                return [seen[subtrahend], index]
            seen[value] = index
        return list()