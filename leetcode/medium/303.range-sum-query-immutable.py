#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#


# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        self.numsArray = nums

    @property
    def prefixSum(self):
        preSum = []
        s = 0
        for i in self.numsArray:
            s += i
            preSum.append(s)
        return preSum

    def sumRange(self, left: int, right: int) -> int:
        smRange = (
            self.prefixSum[right] - self.prefixSum[left]
            if left > 0
            else self.prefixSum[right]
        )
        return smRange


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# @lc code=end
