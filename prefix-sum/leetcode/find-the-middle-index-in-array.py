class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # Calculate the prefix sum for the entire array
        prefix_sum = [0]
        acc = 0
        for num in nums:
            acc += num
            prefix_sum.append(acc)
        for i in range(1,len(nums)+1):
            if prefix_sum[i-1] == prefix_sum[-1] - prefix_sum[i]:
                return i-1
        return -1
         