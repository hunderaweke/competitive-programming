class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counter =defaultdict(int)
        max_score = 0
        running_sum =0
        left = 0

        for right in range(len(nums)):
            running_sum += nums[right]
            counter[nums[right]]  += 1
            while counter[nums[right]] > 1:
                counter[nums[left]] -= 1
                running_sum -= nums[left]
                left += 1
            max_score =max(max_score,running_sum)

        return max_score