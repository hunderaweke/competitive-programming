class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        summ = sum(nums)
        target = summ % p
        if target == 0:
            return 0
        store = {}
        store[0] = -1
        ans = len(nums)+1
        current = 0
        for index in range(len(nums)):
            current += nums[index]
            current %= p
            if (current-target)%p in store:
                ans = min(ans,index-store[(current-target)%p])
            store[current] = index
        if ans >= len(nums):
            return -1
        return ans