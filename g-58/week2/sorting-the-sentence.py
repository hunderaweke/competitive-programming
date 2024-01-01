class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        words.sort(key=lambda x:x[-1])
        words = [word[:len(word)-1] for word in words]
        return ' '.join(words)