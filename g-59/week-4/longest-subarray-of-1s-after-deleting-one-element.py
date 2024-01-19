class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        max_length = 0
        count_zero = 0
        while right < len(nums):
            if nums[right] == 0:
                count_zero += 1
            while count_zero > 1:
                if nums[left] == 0:
                    count_zero -= 1
                left += 1
            max_length = max(max_length, right - left)
            right +=1
        return max_length
