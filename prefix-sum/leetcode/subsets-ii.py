class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subs = set()

        def backtrack(curr,ind):
            subs.add(tuple((sorted(curr[:]))))
            if ind == len(nums):
                return
            for i in range(ind,len(nums)):
                curr.append(nums[i])
                backtrack(curr,i+1)
                curr.pop()
        backtrack([],0)
        return list(subs)
