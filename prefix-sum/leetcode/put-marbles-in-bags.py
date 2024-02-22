class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        adjacent = [weights[i-1]+weights[i] for i in range(1,len(weights))]
        adjacent.sort()
        minimums = 0
        maximums = 0
        for i in range(k-1):
            minimums+=adjacent[i]
            maximums+=adjacent[len(adjacent)-i-1]
        return (maximums-minimums)