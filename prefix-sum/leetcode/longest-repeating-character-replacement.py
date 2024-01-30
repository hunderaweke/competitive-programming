class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts =  {}
        left = 0
        maxFre = 0
        for right,ch in enumerate(s):
            counts[ch] = counts.get(ch,0) + 1
            maxFre = max(maxFre,counts[ch])
            if maxFre + k < right - left + 1:
                counts[s[left]] -= 1
                left += 1
        return len(s) - left