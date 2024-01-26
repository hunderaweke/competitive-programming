class Solution:
    def advance(self,nums,i):
        return (i+nums[i])%len(nums)

    def circularArrayLoop(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        for i, num in enumerate(nums):
            if num ==0 :
                continue
            slow,fast = i,i

            while num*nums[fast] > 0 and num*nums[self.advance(nums,fast)]>0:
                slow = self.advance(nums,slow) 
                fast = self.advance(nums,self.advance(nums,fast)) 

                if slow == fast:
                    if slow == self.advance(nums,slow):
                        break
                    return True
            slow,sign = i,num
            while sign * nums[slow]>0:
                nxt = self.advance(nums,slow)
                nums[slow] = 0
                slow = nxt
        return False
