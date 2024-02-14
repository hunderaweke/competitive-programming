class Solution:
    def maxScore(self, s: str) -> int:
        # construct prefix sum for the zeros and suffix sum for the ones
        zeros = [1 if i == '0' else 0 for i in s]
        ones = [int(i) for i in s]
        for i in range(1,len(s)):
            zeros[i] += zeros[i-1]
        for i in range(len(s)-2,-1,-1):
            ones[i] += ones[i+1]
        ans = 0
        for ptr in range(1,len(s)):
            ans = max(ans,ones[ptr]+zeros[ptr-1])
        return ans