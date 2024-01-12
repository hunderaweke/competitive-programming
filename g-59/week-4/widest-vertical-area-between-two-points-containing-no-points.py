class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        ans = float('-inf')
        for indx in range(1,len(points)):
          diff = points[indx][0] - points[indx-1][0]
          ans = max(diff,ans)
        return ans 