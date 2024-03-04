class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        minimum_unfairness = float('inf')
        def backtrack(distribution,index):
            nonlocal minimum_unfairness
            max_dis = max(distribution)
            if index == len(cookies):
                minimum_unfairness = min(max_dis,minimum_unfairness)
                return 
             
            for i in range(k):
                if minimum_unfairness < max_dis:
                    continue
                distribution[i] += cookies[index]
                backtrack(distribution,index+1)
                distribution[i] -= cookies[index]

        distribution = [0]*k
        backtrack(distribution,0)
        return minimum_unfairness