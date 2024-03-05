class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        
        def find_combinations(start,tot,curr):
            
            if tot == 0:
                combinations.append(curr[:])
                return

            for i in range(start,len(candidates)):
                
                if tot - candidates[i] >= 0:
                    curr.append(candidates[i])
                    find_combinations(i,tot-candidates[i],curr)
                    curr.pop()
                    
        find_combinations(0,target,[])
        
        return combinations
