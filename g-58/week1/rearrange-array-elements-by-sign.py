class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [n for n in nums if n >=0]
        neg = [n for n in nums if n <0]
        for i in range(len(pos)):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]
        return nums