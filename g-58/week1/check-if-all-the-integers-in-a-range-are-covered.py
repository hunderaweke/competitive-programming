class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        rangesCount = [0]*52
        for r in ranges:
            rangesCount[r[0]] +=1
            rangesCount[r[1]+1] -= 1
        for i in range(1,52):
            rangesCount[i] += rangesCount[i-1]
        return 0 not in rangesCount[left:right+1]