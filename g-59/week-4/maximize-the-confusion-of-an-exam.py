class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        counts =  {}
        left = 0
        maxFre = 0
        for right,ch in enumerate(answerKey):
            counts[ch] = counts.get(ch,0) + 1
            maxFre = max(maxFre,counts[ch])
            if maxFre + k < right - left + 1:
                counts[answerKey[left]] -= 1
                left += 1
        return len(answerKey) - left