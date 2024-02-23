class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans  = 0
        for i,num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                idx = stack.pop()
                right = i - idx
                left = idx + 1
                if stack :
                    left = idx - stack[-1]
                ans += left*right*arr[idx]
            stack.append(i)
        while stack:
            idx = stack.pop()
            right = len(arr) - idx
            left = idx + 1
            if stack:
                left = idx - stack[-1]
            ans += left * right *arr[idx]
        return ans %(10**9+7)