class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = sum([num for num in nums if num%2==0])
        ans = []
        for num,index in queries:
            if nums[index] %2 ==0:
                s -= nums[index]
            nums[index] += num
            if nums[index] %2==0:
                s += nums[index]
            ans.append(s)
        return ans