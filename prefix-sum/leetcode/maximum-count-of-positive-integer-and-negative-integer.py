class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            neg = (left + right) // 2
            if nums[neg] < 0:
                left = neg + 1
            else:
                right = neg - 1
        left = neg
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid - 1
        if nums[neg] < 0:
            neg += 1
        if nums[mid] <= 0:
            mid += 1
        return max(neg, len(nums) - mid)
