class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [0]*len(nums)
        res[0], suffix = 1,1
        for i in range(1,len(nums)):
            res[i] = res[i-1]* nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return(res)
        # O(n) additional space solution
        #prefix = [0]*(len(nums)+1)
        #suffix = [0]*(len(nums)+1)
        #res = [0]*len(nums)  
        #prefix[0],suffix[len(nums)] = 1,1
        
        #for n in range(len(nums)):
        #    prefix[n+1] = prefix[n]*nums[n]
        #for n in range(len(nums)-1,-1,-1):
        #   suffix[n] = nums[n]*suffix[n+1]

        #for i in range(len(nums)):
        #    res[i] = prefix[i]*suffix[i+1]
        
        #print(prefix)
        #print(suffix)
        