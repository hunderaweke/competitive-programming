import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i  in range(rowIndex+1):
            comb = (factorial(rowIndex)/(factorial(rowIndex-i)*factorial(i)))
            res.append(int(comb))
        return res
