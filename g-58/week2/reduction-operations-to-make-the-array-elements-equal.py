class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        numsSorted = list(sorted(counter.keys()))
        ans = []
        for i, num in enumerate(numsSorted):
            ans.append(counter[num]*i)
        return sum(ans)