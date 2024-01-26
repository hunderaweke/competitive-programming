class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        res =0 
        hashmap = {0:1}
        for num in nums:
            curSum += num
            res += hashmap.get(curSum - k,0)
            hashmap[curSum] =  hashmap.get(curSum,0) +1
        return res 