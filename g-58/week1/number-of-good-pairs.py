class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt  = defaultdict(int)
        for i in range(len(nums)):
            cnt[nums[i]]+= 1
        ans = sum([math.comb(i,2) for i in cnt.values()])
        return ans