from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = defaultdict(int)
        tMap = defaultdict(int)
        for sChar, tChar in zip(s, t):
            sMap[sChar] += 1
            tMap[tChar] += 1

        for character, frequency in sMap.items():
            if tMap[character] != frequency:
                return False

        return True