class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        _max = max(candies)
        for candy in candies:
            if candy + extraCandies >= _max:
                ans.append(True)
            else:
                ans.append(False)
        return ans