from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        for index in range(len(nums)):
            if index < counter.setdefault(0, 0):
                nums[index] = 0
            elif index < counter.setdefault(0, 0) + counter.setdefault(1, 0):
                nums[index] = 1
            else:
                nums[index] = 2