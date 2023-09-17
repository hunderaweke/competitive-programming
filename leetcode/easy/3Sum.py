// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        for left, num in enumerate(nums):
            if num>0:
                break
            if left>0 and nums[left]==nums[left-1]:
                continue
            mid,right = left+1,len(nums)-1
            while mid<right:
                three = nums[left]+nums[right]+nums[mid]
                if three>0:
                    right-=1
                elif three<0:
                    mid+=1
                else:
                    res.append([nums[left],nums[mid],nums[right]])
                    mid +=1
                    right-=1
                    while nums[mid]==nums[mid-1] and mid<right:
                        mid+=1
        return res


 
            
            
            
            
            
            