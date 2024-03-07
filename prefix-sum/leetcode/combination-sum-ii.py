class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = set()

        def backtrack(ind,curr,tot):
            if tot == target:
                combinations.add(tuple(curr[:]))
                return 
            if ind >= len(candidates) or tot>target:
                return

            for i in range(ind,len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                backtrack(i+1,curr,tot+candidates[i])
                curr.pop()
        
        backtrack(0,[],0)
        return combinations