class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        words = s.split()
        return ' '.join(words[::-1])