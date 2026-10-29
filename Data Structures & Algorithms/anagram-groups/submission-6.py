from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams: List[List[str]] = list()
        collection: Dict = defaultdict(list)
        for index, string in enumerate(strs):
                count = [0] * 26
                for character in string:
                    count[ord(character) - ord('a')] += 1
                collection[tuple(count)].append(index)
                # collection[''.join(sorted(string))].append(index)
        
        for anagrams in collection.values():
            group: List[str] = [strs[index] for index in anagrams]
            grouped_anagrams.append(group)

        return grouped_anagrams
        