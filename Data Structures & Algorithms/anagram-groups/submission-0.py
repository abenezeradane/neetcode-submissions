from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        sorted_strs = ["".join(sorted(string)) for string in strs]
        for index, string in enumerate(sorted_strs):
            hashmap[string].append(strs[index])

        return list(hashmap.values())