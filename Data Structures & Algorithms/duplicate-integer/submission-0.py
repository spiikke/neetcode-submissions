class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dummy = set()
        res = False
        for i in nums:
            if i in dummy:
                res = True
            else:
                dummy.add(i)
        return res

