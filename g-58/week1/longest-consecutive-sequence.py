class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)< 1:
            return 0
        nums.sort()
        length = 1
        left = nums[0]
        count = 1
        for right in range(1,len(nums)):
            if nums[right] == left + 1 :
                count += 1
                length = max(count,length)
            elif nums[right] != left:
                count = 1
            left = nums[right]
        return length