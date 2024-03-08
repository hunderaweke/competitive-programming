class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack  = []
        max_area = 0
        for i, num in enumerate(heights):
            start = i
            while stack and stack[-1][1] > num:
                index,height = stack.pop()
                max_area = max((i-index)*height,max_area)
                start = index
            stack.append((start,num))
        for index,height in stack:
            max_area = max((len(heights)-index)*height,max_area)
        return max_area