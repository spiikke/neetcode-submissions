class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for n in range(len(nums)-2):
            if nums[n] > 0:
                break

            if n>0 and nums[n] == nums[n-1]:
                continue

            l,r = n+1, len(nums)-1
            while l<r:
                threeSum = nums[n] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                    continue
                elif threeSum < 0:
                    l += 1
                    continue
                else:
                    res.append([nums[n],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
        return res



        