class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # upper bound max(piles) = k
        # lower bound = 1
        # searching for min k

        l , r = 1 , max(piles)

        while l < r:
            t = 0
            k = (l+r)//2

            for i in piles:
                if k > i:
                    t += 1
                else:
                    t += i // k
                    t += 1 if i % k > 0 else 0 
            
            if t <= h:
                r = k
            else:
                l = k + 1
        return l
            
                
    