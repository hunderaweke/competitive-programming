class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subs = []

        def backtrack(curr,ind):
            if ind == len(nums):
                subs.append(curr[:])
                return
            subs.append(curr[:])
            for i in range(ind,len(nums)):
                curr.append(nums[i])
                backtrack(curr,i+1)
                curr.pop()
        backtrack([],0)
        return subs
