class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left,right = 0,n - 1
        best = 0
        while left <= right:
            mid = left + (right-left) // 2
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] > n - mid:
                right = mid-1
            else:
                left = mid+1
        return n - left 