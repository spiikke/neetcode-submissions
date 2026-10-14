class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            if stack and stack[-1][0] >= temp:
                stack.append([temp,i])
            elif stack:
                while stack and temp > stack[-1][0]:
                    cur = stack.pop()
                    res[cur[1]] = i - cur[1]
                stack.append([temp,i])
            else:
                stack.append([temp,i])
        return res
            

        