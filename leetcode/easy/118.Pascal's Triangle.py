class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for rowIndex in range(numRows):
            row = [1]
            prev = 1
            for j in range(1,rowIndex+1):
                val = (prev * (rowIndex-j+1))//j
                prev = val
                row.append(val)
            res.append(row)
        return res
