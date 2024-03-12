class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        lower = points[0][0]
        upper = points[0][1]
        required_arrows = 1
        for interval in points:
            if interval[0] >= lower and interval[0] <= upper:
                lower = interval[0]
                upper = min(upper, interval[1])
            else:
                lower = interval[0]
                upper = interval[1]
                required_arrows += 1
        return required_arrows