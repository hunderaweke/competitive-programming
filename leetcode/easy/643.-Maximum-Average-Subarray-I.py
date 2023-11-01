class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = sum(nums[:k])
        ave = res / k
        for i in range(len(nums)-k):
            res = res - nums[i]+nums[i+k]
            ave = max(ave,res/k) 
        return ave
