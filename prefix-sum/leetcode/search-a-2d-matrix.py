class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        left,right = 0,rows * cols-1

        while left <= right:
            mid = left + (right - left) //2

            col = mid % cols
            row = mid // cols

            if matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                return True
                
        return False

