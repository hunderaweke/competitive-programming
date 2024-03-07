import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        prev = 1
        for i  in range(1,rowIndex+1):
            comb = (prev * (rowIndex -i+1)) //i
            prev = comb
            res.append(int(comb))
        return res