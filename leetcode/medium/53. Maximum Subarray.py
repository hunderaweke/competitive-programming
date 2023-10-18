class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        maxL,maxR = 0,0
        L =0
        for R in range(len(nums)):
            if curSum<0:
                curSum = 0
                L= R
            curSum+=nums[R]
            if curSum>maxSum:
                maxSum = curSum
                maxL,maxR = L,R
        return maxSum
