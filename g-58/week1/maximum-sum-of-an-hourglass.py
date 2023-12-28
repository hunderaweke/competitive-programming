class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # Initialize pre_sum
        pre_sum = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        
        # Calculate prefix sum
        for row in range(1, rows+1):
            for col in range(1, cols+1):
                pre_sum[row][col] = pre_sum[row][col-1] + pre_sum[row-1][col] - pre_sum[row-1][col-1] + grid[row-1][col-1]
        
        max_glass = float('-inf')
        
        for row in range(3, rows+1):
            for col in range(3, cols+1):
                reduced = grid[row-2][col-1] + grid[row-2][col-3]
                glass_sum = pre_sum[row][col] + pre_sum[row-3][col-3] - pre_sum[row-3][col] - pre_sum[row][col-3] - reduced
                max_glass = max(max_glass, glass_sum)
        
        return max_glass
