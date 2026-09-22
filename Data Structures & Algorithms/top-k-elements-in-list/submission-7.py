from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        array = []
        counter = Counter(nums)

        for key, value in counter.items():
            array.append((value, key))

        array.sort(reverse=True)
        return [number for _, number in array[:k]]