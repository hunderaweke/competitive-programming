class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        preSum = [0] * len(nums)
        sufSum =[0] * len(nums)
        preSum[0] = nums[0]
        for i in range(1,len(nums)):
            preSum[i] += preSum[i-1] + nums[i]
        sufSum[len(nums)-1] = nums[len(nums) - 1]
        for i in range(len(nums)-2,-1,-1):
            sufSum[i] += sufSum[i+1] + nums[i]
        for i in range(len(nums)):
            leftSum = nums[i]*(i+1) - preSum[i]
            rightSum = sufSum[i] - (nums[i]*(len(nums)-i))
            ans[i] = leftSum + rightSum
        return ans