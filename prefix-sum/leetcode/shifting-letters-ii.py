class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        indices = [0]*len(s)
        for left,right,direction in shifts:
            if direction == 1:
                indices[left] += 1
                if right+1<len(s):
                    indices[right+1] -= 1
            else:
                indices[left] -= 1
                if right+1<len(s):
                    indices[right+1] += 1
        acc = 0
        for idx in range(len(indices)):
            acc += indices[idx]
            indices[idx] = acc
        ans =[]
        for idx in range(len(s)):
            new = (ord(s[idx])+indices[idx]-ord('a'))%26
            new += ord('a')
            ans.append(chr(new))
        return "".join(ans)