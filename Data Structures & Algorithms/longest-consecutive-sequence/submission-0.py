class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            l = 0
            if n-1 not in numSet:
                while n+l in numSet:
                    l += 1
                longest = max(l,longest)
        return longest
