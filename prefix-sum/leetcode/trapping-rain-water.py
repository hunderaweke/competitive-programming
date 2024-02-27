class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        res = 0
        running_sum  = 0
        right = left
        max_height = max(height)
        max_index  = height.index(max_height)
        while right <= max_index:
            if height[right] < height[left]:
                running_sum += (height[left] - height[right])
            elif height[right] >= height[left]:
                res += running_sum
                running_sum = 0
                left = right
            right += 1
        rel_max = height[-1]
        running_sum = 0
        for right in range(len(height) - 1, max_index, -1):
            if height[right] > rel_max:
                rel_max = height[right]
            else:
                running_sum += rel_max - height[right]
        res += running_sum
        return res