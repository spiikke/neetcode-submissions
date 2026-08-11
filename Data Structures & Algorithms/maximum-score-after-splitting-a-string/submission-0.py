class Solution:
    def maxScore(self, s: str) -> int:
        l = 0
        r = s.count("1")
        maximum = 0

        for i in range(len(s)-1):
            if int(s[i]) == 0:
                l += 1
            else:
                r -= 1
            maximum = max(maximum,l+r)
        return maximum

        