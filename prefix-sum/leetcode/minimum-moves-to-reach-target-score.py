class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        doubling = 0
        increments = 0
        while target > 2 and doubling < maxDoubles:
            increments += target%2
            target //=2
            doubling+=1
        
        return increments+doubling+target-1