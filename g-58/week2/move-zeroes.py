class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      """
      Do not return anything, modify nums in-place instead.
      """
      placeHolder,seeker = 0,1
      while seeker < len(nums):
        if placeHolder == len(nums):
          break
        elif (nums[placeHolder] == 0 and nums[seeker]!=0) and placeHolder < seeker:
          nums[placeHolder],nums[seeker] = nums[seeker],nums[placeHolder]
        while placeHolder < len(nums) and nums[placeHolder] != 0:
          placeHolder +=1
        seeker += 1
        