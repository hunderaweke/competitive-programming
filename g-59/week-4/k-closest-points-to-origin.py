class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
      def distance(point:List[int]) -> float:
        return (point[0]**2 + point[1]**2)**0.5
      points.sort(key=distance)
      return points[:k]