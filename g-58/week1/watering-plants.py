class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans  = 0
        initial = capacity
        for right in range(len(plants)):
            if capacity < plants[right]:
                capacity = initial
                ans+=(right*2)
            capacity -= plants[right]
            ans+=(1)
        return ans
