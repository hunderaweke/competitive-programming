class Solution:
    def findMin(self, nums: List[int]) -> int:
        curr_min = nums[0]
        left,right = 0,len(nums)-1
        curr_min = min(curr_min,nums[left],nums[right])
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > curr_min:
                left = mid + 1
            else:
                curr_min = min(curr_min,nums[mid])
                right = mid - 1
        return curr_min