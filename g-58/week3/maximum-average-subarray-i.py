class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float('-inf')
        left = 0
        running_sum = 0
        for right in range(len(nums)):
            running_sum += nums[right]
            if right - left + 1 > k:
                running_sum -= nums[left]
                left += 1
            if right - left + 1 == k:
                res = max(res,running_sum)
        return res / k