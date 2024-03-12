class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        running_sum = nums[0]
        for i in range(1,len(nums)):
            running_sum += nums[i]
            if nums[i] > ans:
                ans = max(ans,ceil(running_sum / (i+1)))
        return ans