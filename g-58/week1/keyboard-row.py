class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row  = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        ans  = []
        for word in words:
            if word[0].lower() in first_row:
                row = first_row
            elif word[0].lower() in second_row:
                row = second_row
            elif word[0].lower() in third_row:
                row = third_row
            can_be = True
            for char in word:
                if char.lower() not in row:
                    can_be = False
            if can_be:
                ans.append(word)
        return ans