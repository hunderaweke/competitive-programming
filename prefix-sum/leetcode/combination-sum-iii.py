class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1,10))
        combinations = []

        def backtrack(ind,curr,tot):
            if len(curr) == k and tot == n:
                combinations.append(curr[:])
                return
            
            if len(curr) >= k or ind >= len(nums) or tot > n:
                return
            
            for i in range(ind,len(nums)):
                curr.append(nums[i])
                backtrack(i+1,curr,tot+nums[i])
                curr.pop()
        
        backtrack(0,[],0)
        return combinations