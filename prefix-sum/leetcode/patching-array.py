class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        patch = 0
        index = 0
        while miss <= n:
            if index < len(nums)and  miss >= nums[index]:
                miss += nums[index]
                index += 1
            else:
                patch += 1
                miss += miss
        return patch