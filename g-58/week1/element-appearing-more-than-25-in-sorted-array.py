class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = Counter(arr)
        for num in counter:
            if counter[num] > len(arr)/4:
                return num