class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        left = 0
        CONST = ord("a")
        for right in range(2,len(s)):
            if s[right] == "#":
                while right-left + 1 > 3:
                    res += chr(CONST+int(s[left])-1)
                    left += 1
                res += chr(CONST + int(s[left:right])-1)
                left = right + 1
        while left < len(s):
            res += chr(CONST+int(s[left])-1)
            left += 1
        return res