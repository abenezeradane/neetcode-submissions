from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        array = []
        hashmap = defaultdict(int)
        for number in nums:
            hashmap[number] += 1

        for key, value in hashmap.items():
            array.append((value, key))

        array.sort(reverse=True)
        return [number for _, number in array[:k]]