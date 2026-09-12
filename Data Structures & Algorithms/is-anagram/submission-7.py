class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}
        for sChar, tChar in zip(s, t):
            if sChar not in hashmap:
                hashmap[sChar] = (1, 0)
            else:
                sCharFreq = list(hashmap[sChar])
                sCharFreq[0] += 1
                hashmap[sChar] = tuple(sCharFreq)

            if tChar not in hashmap:
                hashmap[tChar] = (0, 1)
            else:
                tCharFreq = list(hashmap[tChar])
                tCharFreq[1] += 1
                hashmap[tChar] = tuple(tCharFreq)

        for frequency in hashmap.values():
            if frequency[0] != frequency[1]:
                return False

        return True