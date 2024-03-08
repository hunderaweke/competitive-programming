class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        upper_bound = sum(nums)
        lower_bound = max(nums)
        best = sum(nums)
        while upper_bound >= lower_bound:
            mid = (upper_bound + lower_bound)//2

            calculated_division = 1
            curr_sum = 0
            for num in (nums):
                curr_sum += num
                if curr_sum > mid:
                    calculated_division += 1
                    curr_sum = num
            
            if calculated_division > k:
                lower_bound = mid + 1
            else:
                upper_bound = mid - 1
                best = mid
        return best