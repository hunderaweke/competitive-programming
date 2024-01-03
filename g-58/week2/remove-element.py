class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      placeHolder,seeker = 0,1
      while seeker < len(nums) and placeHolder<len(nums):
        if (nums[placeHolder]==val and nums[seeker] != val) and (placeHolder < seeker):
          nums[placeHolder],nums[seeker] = nums[seeker],nums[placeHolder]
        while placeHolder < len(nums) and nums[placeHolder] != val:
          placeHolder += 1
        seeker +=1
      while nums.count(val):
        nums.pop()