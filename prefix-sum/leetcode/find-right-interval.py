class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        indices = {start: i for i, (start, _) in enumerate(intervals)}
        starts = [start for start, _ in intervals]
        starts.sort()
        n = len(intervals)
        ans = [-1] * n

        for i, (_, end) in enumerate(intervals):
            index = bisect_left(starts, end)
            if index < n:
                ans[i] = indices[starts[index]]
        return ans