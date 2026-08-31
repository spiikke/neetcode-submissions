class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(":")","{":"}","[":"]"}
        for char in s:
            if char in pairs.keys():
                stack.append(pairs[char])
            else:
                if stack:
                    if stack[-1] == char:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return not stack


        