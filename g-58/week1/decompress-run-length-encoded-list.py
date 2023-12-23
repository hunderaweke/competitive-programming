class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans  = []
        ptr1,ptr2 = 0,1
        while ptr2 < len(nums):
            for i in range(nums[ptr1]):
                ans.append(nums[ptr2])
            ptr1 += 2
            ptr2 += 2
        return ans