class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2
        for index, value in enumerate(nums):
            ans[index] = value
            ans[index + len(nums)] = value
        return ans