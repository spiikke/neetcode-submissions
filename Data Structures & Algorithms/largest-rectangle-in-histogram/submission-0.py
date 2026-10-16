class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # (index,height)
        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                area = (i - index)*height
                maxArea = max(maxArea,area)
                start = index
            stack.append((start,h))
        while stack:
            index, height = stack.pop()
            area = (len(heights)- index)*height
            maxArea = max(maxArea,area)
        return maxArea
            
            