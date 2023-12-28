class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        ans = []
        for num in arr2:
            ans.extend([num]*counter[num])
            counter.pop(num)
        left = sorted(counter.keys())
        for num in left:
            ans.extend([num]*counter[num])
            counter.pop(num)
        return ans