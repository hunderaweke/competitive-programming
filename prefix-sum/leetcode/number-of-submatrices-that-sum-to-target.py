class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ROWS,COLS = len(matrix),len(matrix[0])
        prefix = [[0 for _ in range(COLS+1)] for _ in range(ROWS+1)]
        for row in range(ROWS):
            for col in range(COLS):
                above = prefix[row][col+1]
                behind = prefix[row+1][col]
                top_right = prefix[row][col]
                prefix[row+1][col+1] += above + behind - top_right + matrix[row][col]
        ans  =0 
        for r1 in range(1,ROWS+1):
            for r2 in range(r1,ROWS+1):
                hash_map = defaultdict(int)
                hash_map[0] += 1
                for col in range(1,COLS+1):
                    current = prefix[r2][col] - prefix[r1-1][col]-target
                    ans += hash_map[current]
                    hash_map[prefix[r2][col] - prefix[r1-1][col]] += 1
        return ans