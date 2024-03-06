class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        def find_ads(row,col):
            ads = []
            if row > 0:
                ads.append((row-1,col))
            if row < rows-1:
                ads.append((row+1,col))
            if col > 0:
                ads.append((row,col-1))
            if col < cols-1:
                ads.append((row,col+1))
            return ads
        # Since the word can only beformed using the adjacent letters we just need to find the adjacent letters
        visited = set()
        def find_word(ind,row,col):
            if ind == len(word):
                return True

            if ind == len(word)-1 and word[ind] == board[row][col]:
                return True

            if word[ind] != board[row][col]:
                return False

            visited.add((row,col))
            adjacents = find_ads(row,col)

            for r,c in adjacents:
                if (r,c) not in visited:
                    if find_word(ind+1,r,c):
                        return True

            visited.remove((row,col))
            
            return False
        
        # Since we are not sure to where we should start we need to check each of the indices as a startins points

        for row in range(rows):

            for col in range(cols):
                    
                if find_word(0,row,col):

                    return True
    
        return False