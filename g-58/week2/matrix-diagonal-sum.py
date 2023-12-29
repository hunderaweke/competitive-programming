class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # find the number of cols and rows
        # Make a hashmap for storing the diagonals both for the primary and secondary
        # Add the diagonals to the Hashset 
        # return the sum of the hashset
        # Since the matrix is square the diagonals will be at the place of the rows
        diagonals = defaultdict(set)
        rows,cols = len(mat),len(mat[0])-1
        for row in range(rows):
            diagonalPri = mat[row][row]
            diagonalSec = mat[row][cols-row]
            diagonals[diagonalPri].add((row,row))
            diagonals[diagonalSec].add((row,cols-row))
        diagonal_sum = 0
        for num in diagonals:
            diagonal_sum += len(diagonals[num])* num
        return diagonal_sum