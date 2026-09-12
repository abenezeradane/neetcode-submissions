from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)
        for number in nums:
            if number in hashmap:
                return True
            hashmap[number] += 1
        return False