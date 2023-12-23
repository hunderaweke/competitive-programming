class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = [n for n in nums if n <pivot]
        greater = [n for n in nums if n >pivot]
        equal = [n  for n in nums if n==pivot]
        return less +equal+ greater