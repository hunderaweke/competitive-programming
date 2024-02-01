class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1]+num)
        count = defaultdict(int)
        ans =0
        for pre in preSum:
            ans += count[pre]
            count[pre+goal] += 1
        return ans