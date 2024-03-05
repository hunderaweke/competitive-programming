class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        left =0
        counter = defaultdict(int)
        ans = 0
        for right,num in enumerate(nums):
            counter[num] += 1

            while len(counter) == distinct:
                counter[nums[left]] -= 1
                if not counter[nums[left]]:
                    counter.pop(nums[left])
                left += 1

            ans += left
        
        return ans