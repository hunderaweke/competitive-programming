class Solution:
    def totalNQueens(self, n: int) -> int:
        rows = set()
        cols = set()
        posDiagonals = set()
        negDiagonals = set()
        board = [["."]*n for _ in range(n)]
        count = 0
        def backtrack(row,queens):
            nonlocal count
            if queens == 0:
                count += 1
                return
            
            if row >= n:
                return
            
            for col in range(n):
                if col in cols or row+col in posDiagonals or row-col in negDiagonals or row in rows:
                    continue
                rows.add(row)
                cols.add(col)
                posDiagonals.add(row+col)
                negDiagonals.add(row-col)
                backtrack(row+1,queens - 1)
                rows.remove(row)
                cols.remove(col)
                posDiagonals.remove(row+col)
                negDiagonals.remove(row-col)
        backtrack(0,n)
        return count