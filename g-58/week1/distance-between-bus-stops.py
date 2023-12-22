class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        _min = min(start,destination)
        _max = max(start,destination)
        return min(sum(distance[_min:_max]),sum(distance[:_min]+distance[_max:]))