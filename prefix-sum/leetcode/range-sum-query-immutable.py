class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.preSum = [0]
        running_sum = 0
        for num in self.nums:
            running_sum+=num
            self.preSum.append(running_sum)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right+1]-self.preSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)