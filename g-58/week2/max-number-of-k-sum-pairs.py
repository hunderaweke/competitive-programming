class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
      nums.sort()
      right,left = len(nums)-1,0
      res = 0
      while left < right:
        _sum = nums[left] + nums[right]
        if _sum == k:
          res += 1
          right -= 1
          left += 1
        elif _sum < k:
          left += 1
        elif _sum > k:
          right -=1
      return res