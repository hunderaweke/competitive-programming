class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count_zeros = 0
        left = 0
        max_length = 0
        for right in range(len(nums)):
            count_zeros += nums[right]==0
            while count_zeros > k:
                count_zeros -= nums[left] == 0
                left += 1
            max_length = max(max_length,right-left+1)
        return max_length