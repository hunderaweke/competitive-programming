class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(image)):
            row = image[i][::-1]   
            for j in range(len(row)):
                if row[j]:
                    row[j] = 0
                else:
                    row[j] = 1
            ans.append(row)
        return ans