class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left,right = 0, len(height)-1
        while left < right:
            temp = min(height[left],height[right])*(right-left)
            if height[left] < height[right]:
                left+=1
            elif height[left] >= height[right]:
                right-=1
            res = max(temp,res)
        return res  
