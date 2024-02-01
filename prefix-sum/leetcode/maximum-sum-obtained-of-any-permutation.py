class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        requests_visit = [0]*n
        for left,right in requests:
            requests_visit[left] += 1
            if right +1<n:
                requests_visit[right+1]-=1
        for i in range(1,n):
            requests_visit[i] += requests_visit[i-1]
        requests_visit.sort()
        nums.sort()
        ans = 0
        for i in range(n):
            ans += nums[i]*requests_visit[i]
        return ans % ((10**9)+7)