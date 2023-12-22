class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans  = 0
        for i in range(len(nums)-2):
            a,b,c = nums[i+2],nums[i+1],nums[i]
            if a+b>c:
                ans  = max(ans,a+b+c)
        return ans    