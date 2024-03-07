class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows = set()
        cols = set()
        negDiagonals = set()
        posDiagonals = set()
        ans = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def backtrack(row, queens):
            if queens == n:
                temp = ["".join(r) for r in board]
                ans.append(temp[:])
                return

            if row >= n:
                return

            for c in range(n):
                if (
                    row + c in posDiagonals
                    or row - c in negDiagonals
                    or c in cols
                ):
                    continue
                board[row][c] = "Q"
                rows.add(row)
                cols.add(c)
                posDiagonals.add(row + c)
                negDiagonals.add(row - c)
                backtrack(row + 1, queens + 1)
                board[row][c] = "."
                rows.remove(row)
                cols.remove(c)
                posDiagonals.remove(row + c)
                negDiagonals.remove(row - c)

        backtrack(0, 0)
        return ans
