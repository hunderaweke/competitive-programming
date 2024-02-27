class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        number_of_operations = 0
        current_min = nums[-1]
        for idx in range(len(nums)-1,-1,-1):
            if nums[idx] <= current_min:
                current_min = nums[idx]
                continue
            
            number_of_elements = ceil(nums[idx]/current_min) 
            number_of_operations += number_of_elements - 1
            current_min = nums[idx]//number_of_elements
        return number_of_operations