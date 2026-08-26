class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        prev = 0
        for i in range(len(nums)-1):
            if nums[i] > 0:
                break
            if i != 0 and nums[i] == nums[i-1]:
                continue
            fixed = nums[i]
            target = (-1)*nums[i]
            l = i+1
            r = len(nums)-1
            while l<r:
                if nums[l] + nums[r] == target:
                    res.append([fixed,nums[l],nums[r]])
                    l += 1
                    r -= 1 
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
            fixed = nums[i+1]
        return res


        