class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end  = -1
        left,right = 0,len(nums)-1
        # For finding the first index for the range number
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                start = mid 
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left,right = 0,len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                end = max(end,mid)
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return [start,end]