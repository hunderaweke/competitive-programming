class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right  = 1
        while right<len(nums):
            if nums[right] == nums[left]:
                nums.pop(left)
            else:
                left = right
                right += 1