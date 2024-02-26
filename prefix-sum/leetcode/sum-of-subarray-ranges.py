class Solution:
    def subArrayRanges(self, arr: List[int]) -> int:
        # since we can find the sums of the ranges we can use the sum of minimums of a specific subarray size and the maximums as well
        # find the sums of that subarray both of the minimums and maximums and the subtractation of the two will be the answer
        stack = []
        minimums  = 0
        for i,num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                idx = stack.pop()
                right = i - idx
                left = idx + 1
                if stack :
                    left = idx - stack[-1]
                minimums += left*right*arr[idx]
            stack.append(i)
        while stack:
            idx = stack.pop()
            right = len(arr) - idx
            left = idx + 1
            if stack:
                left = idx - stack[-1]
            minimums += (left * right) *arr[idx]
        stack = []
        maximums = 0
        for i,num in enumerate(arr):
            while stack and arr[stack[-1]] < num:
                idx = stack.pop()
                right = i - idx
                left = idx + 1
                if stack:
                    left = idx - stack[-1]
                maximums+= left*right*arr[idx]
            stack.append(i)
        while stack:
                idx = stack.pop()
                right = len(arr) - idx
                left = idx + 1
                if stack:
                    left = idx - stack[-1]
                maximums+= left*right*arr[idx]
        return maximums - minimums            