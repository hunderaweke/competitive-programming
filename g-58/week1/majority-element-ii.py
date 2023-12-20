class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [i for i in counter if counter[i] > (len(nums)//3)]