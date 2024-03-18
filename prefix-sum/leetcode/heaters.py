class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def condition(radius) -> bool:
            for house in houses:
                pos = bisect_right(heaters, house)
                upper = lower = True
                if pos < len(heaters):
                    if heaters[pos] - radius > house:
                        upper = False
                else:
                    upper = False
                if pos > 0:
                    if heaters[pos - 1] + radius < house:
                        lower = False
                else:
                    lower = False
                if not (upper or lower):
                    return False
            return True

        left, right = 0, max(max(houses) - min(heaters), max(heaters) - min(houses))

        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left