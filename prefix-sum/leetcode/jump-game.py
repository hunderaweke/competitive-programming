class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) > 1:
            return False
        if len(nums) == 1:
            return True
        prev = 0
        for i in range(len(nums)-1):
            prev = max(prev,(nums[i]+i))
            if prev == i and nums[i] ==0:
                return False
            if nums[i] + i >= len(nums)-1:
                return True
        return False