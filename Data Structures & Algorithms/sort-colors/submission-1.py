from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        zero = [0] * (counter.setdefault(0, 0))
        one = [1] * (counter.setdefault(1, 0))
        for index in range(len(nums)):
            if index < len(zero):
                nums[index] = 0
            elif index < len(zero) + len(one):
                nums[index] = 1
            else:
                nums[index] = 2