class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def fingerprint(word: str) -> List[str]:
            fingerprint = [0]*26
            for char in word:
                fingerprint[ord(char)- ord('a')] += 1
            return fingerprint
        
        freq = {}
        for word in strs:
            f = tuple(fingerprint(word))
            if f in freq:
                freq[f].append(word)
            else:
                freq[f] = [word]
        res = list(freq.values())

        return res
        