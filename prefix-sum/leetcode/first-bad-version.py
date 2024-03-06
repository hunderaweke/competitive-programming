# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first_bad = n
        left,right = 0,n
        while left <=  right:
            mid = left + (right-left)//2
            if isBadVersion(mid):
                first_bad = min(first_bad,mid)
                right = mid - 1
            else:
                left = mid + 1
        return first_bad