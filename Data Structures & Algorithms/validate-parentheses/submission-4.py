class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(':')','{':'}','[':']'}
        
        for char in s:
            if char in pairs:
                stack.append(pairs[char])
            else:
                if not stack:
                    return False
                elif stack[-1] == char:
                    stack.pop()
                else:
                    return False
        return not stack

    