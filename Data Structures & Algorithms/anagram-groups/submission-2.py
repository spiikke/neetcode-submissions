class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            fingerprint = [0]*26
            for char in word:
                index = ord(char) - ord('a')
                fingerprint[index] += 1
            x = tuple(fingerprint)
            if x  not in groups:
                groups[x] = []
            groups[x].append(word)
        return list(groups.values())