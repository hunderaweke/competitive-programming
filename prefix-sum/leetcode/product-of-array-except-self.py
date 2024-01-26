class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1]*len(nums)
        for i in range(1,len(nums)):
            prefix_product[i] *= prefix_product[i-1]*nums[i-1]
        suffix_product = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            suffix_product[i] *= suffix_product[i+1]*nums[i+1]
        ans = [1]*len(nums)
        for i in range(len(nums)):
            ans[i] *= prefix_product[i]*suffix_product[i]
        return ans
        