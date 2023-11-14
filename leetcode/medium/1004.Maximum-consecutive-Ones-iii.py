class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        counter = 0
        left =0 
        for right in range(len(nums)):
            if nums[right] == 0:
                counter+= 1
            while counter > k:
                if nums[left] ==0 :
                    counter -= 1
                left +=1
            res = max(res,right - left +1)
        return res
