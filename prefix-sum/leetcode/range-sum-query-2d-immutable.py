class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        for row in range(len(matrix)):
            previous = 0
            for col in range(len(matrix[0])):
                previous += matrix[row][col]
                above = self.prefix_sum[row][col+1]
                self.prefix_sum[row+1][col+1] = previous+above
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2 = row1+1,col1+1,row2+1,col2+1
        bottom_right = self.prefix_sum[row2][col2]
        above = self.prefix_sum[row1-1][col2]
        left = self.prefix_sum[row2][col1-1]
        top_left=self.prefix_sum[row1-1][col1-1]
        return bottom_right-above-left+top_left



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)