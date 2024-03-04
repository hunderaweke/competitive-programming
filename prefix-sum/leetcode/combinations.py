class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []


        def dfs(start,curr_combination):
            if len(curr_combination) == k:
                result.append(curr_combination[:])
                return
    
            for num in range(start,n+1):
                curr_combination.append(num)
                dfs(num+1,curr_combination)
                curr_combination.pop()

        dfs(1,[])
        return result