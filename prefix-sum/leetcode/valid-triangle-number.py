class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        combinations = 0
        for i in range(1,len(nums)):
            left,right = 0, i -1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    combinations += right-left
                    right -=1
                else:
                    left += 1
        return combinations