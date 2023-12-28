class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = len(strs[0])
        rows = len(strs)
        unsorted = 0
        for col in range(cols):
            for row in range(1,rows):
                if strs[row][col] < strs[row-1][col]:
                    unsorted += 1
                    break
        return unsorted
