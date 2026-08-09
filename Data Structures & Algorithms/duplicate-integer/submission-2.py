class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        p1 = 0 
        p2 = 1
        for i in range(len(nums)-1):
            if nums[p1] == nums[p2]:
                return True
            p1 += 1
            p2 += 1    
        return False

        