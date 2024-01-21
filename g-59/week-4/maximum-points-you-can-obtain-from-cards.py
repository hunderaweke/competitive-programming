class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        m = len(cardPoints)-k
        _sum = sum(cardPoints)
        left = 0
        max_points = 0
        running_sum = 0
        for right in range(len(cardPoints)):
            running_sum += cardPoints[right]
            while right - left + 1> m:
                running_sum -= cardPoints[left]
                left += 1
            if right - left + 1 == m:
                max_points = max(max_points,_sum-running_sum)
        return max_points