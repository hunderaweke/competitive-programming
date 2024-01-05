class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        dis,ans = float('inf'),float('inf')
        for i , num in enumerate(nums):
            if i > 0 and nums[i-1] == num:continue
            left,right = i+1,len(nums)-1
            while left < right:
                threeSum = num + nums[left] + nums[right]
                currDis = abs(target - threeSum)
                if currDis < dis:
                    ans= threeSum
                    dis = currDis
                if threeSum == target:
                    return target
                elif threeSum < target:
                    left += 1
                else:
                    right -= 1
        return ans
