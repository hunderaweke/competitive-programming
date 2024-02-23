class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_queue = deque()
        left = 0
        ans  = []
        for right,num in enumerate(nums):
            while max_queue and max_queue[-1] < num:
                max_queue.pop()
            max_queue.append(num)
            if right - left + 1 >= k:
                ans.append(max_queue[0])
                if nums[left] == max_queue[0]:
                    max_queue.popleft()
                left += 1
        return ans
