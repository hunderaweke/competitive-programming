class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagram = tuple(sorted(p))
        left = 0
        res = []
        for right in range(len(s)):
            while right - left + 1 > len(p):
                left += 1
            if right - left + 1 == len(p):
                if tuple(sorted(s[left:right +1])) == anagram:
                    res.append(left)
            
        return res