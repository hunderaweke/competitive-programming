class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        nice_subarrays = 0
        current_count = 0
        # Iterate ove the whole array for counting the length of the nice subarrays

        for right in range(len(nums)):
            # Checking if the number is a number is odd and reinitializing the count for next iteration counting
            if nums[right]%2 != 0:
                current_count += 1
                count = 0
            if current_count == k:
                # check if the number at left is even and increment left while True since this doesn't effect our current_counter
                while left < len(nums) and nums[left] % 2 ==0:
                    count+=1
                    left += 1
                # if the number is odd increment the count by one
                count += 1
                current_count -= 1
                left += 1
            nice_subarrays += count
        return nice_subarrays
            

