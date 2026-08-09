class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def makeDict(x: str) -> dict:
            count = {}            
            for char in x:
                if char in count:
                    count[char]+=1
                else:
                    count[char]=1
            return count

        return makeDict(s) == makeDict(t) 