class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = deque()
        max_queue = deque()
        ans = 1
        left = 0
        for right, num in enumerate(nums):
            # building the minimum queue monotonically increasing
            while min_queue and min_queue[-1] > num:
                min_queue.pop()
            min_queue.append(num)
            # building the minimum queue monotonically decreasing
            while max_queue and max_queue[-1] < num:
                max_queue.pop()
            max_queue.append(num)
            while max_queue[0] - min_queue[0] > limit:
                if nums[left] == max_queue[0]:
                    max_queue.popleft()
                if nums[left] == min_queue[0]:
                    min_queue.popleft()
                left += 1
            ans = max(ans, right - left + 1)
        return ans