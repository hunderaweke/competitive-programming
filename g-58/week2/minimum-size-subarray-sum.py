class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        running_sum = 0
        res = float('inf')
        for right in range(len(nums)):
            running_sum += nums[right]
            while running_sum >= target:
                res = min(right - left + 1 , res)
                running_sum -= nums[left]
                left += 1
        return res if res != float('inf') else 0
        