class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = 0
        for row in range(len(matrix)):
            for col in range(row,len(matrix)):
                matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col]
        for row in matrix:
            row.reverse()