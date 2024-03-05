class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def backtrack(arr,curr):
            if len(curr) == len(nums):
                result.append(curr[:])
                return
            
            if len(arr) == 0:
                return 
            
            for i in range(len(arr)):
                curr.append(arr[i])
                backtrack(arr[:i]+arr[i+1:],curr)
                curr.pop()
    
        backtrack(nums,[])
        return result
            
