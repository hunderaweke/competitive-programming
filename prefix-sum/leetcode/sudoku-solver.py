class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_box(row,col):
            if row < 3:
                if col < 3:
                    return 0
                elif col < 6:
                    return 1
                else:
                    return 2
            if row < 6:
                if col < 3:
                    return 3
                elif col < 6:
                    return 4
                else:
                    return 5
            if row < 9 :
                if col < 3:
                    return 6
                elif col < 6:
                    return 7
                else:
                    return 8
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        for i in range(9):
            for j in range(9):
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box_index = get_box(i,j)
                box[box_index].add(board[i][j])
        def next_index(row,col):
            if col < 8:
                return row,col+1
            else:
                return row+1,0
        
        def backtrack(i,j):
            if i >= 9:
                return True
            if board[i][j] != ".":
                x,y = next_index(i,j)
                return backtrack(x,y)
            
            box_index = get_box(i,j)
            for n in range(1,10):
                num = str(n)
                if str(n) not in box[box_index] and  str(n) not in row[i] and str(n) not in col[j]:
                    board[i][j] = num
                    box[box_index].add(num)
                    row[i].add(num)
                    col[j].add(num)
                    x,y = next_index(i,j)
                    solved = backtrack(x,y)
                    if solved:
                        return True 
                    board[i][j] = "."
                    row[i].remove(num)
                    col[j].remove(num)
                    box[box_index].remove(num)
            return False 
        print(backtrack(0,0))
