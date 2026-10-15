class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for n in range(len(position)):
            pair.append((position[n],speed[n]))
        pair.sort(reverse=True)
        
        times = []
        for p in pair:
            time = (target-p[0])/p[1]
            times.append(time)
        
        stack = []
        for t in times:
            if stack and stack[-1] >= t:
                continue
            else:
                stack.append(t)
        
        return len(stack)