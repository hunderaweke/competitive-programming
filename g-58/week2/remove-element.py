class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        if val in nums:
            l = nums.index(val)
            r = l+1
            n = nums.count(val)
        else:
            return len(nums)
        while r<len(nums):
            if nums[l] == nums[r] and r<len(nums):
                r+=1
            elif nums[l]< nums[r]:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r+=1
                n -=1
        return len(nums)- nums.count(val)