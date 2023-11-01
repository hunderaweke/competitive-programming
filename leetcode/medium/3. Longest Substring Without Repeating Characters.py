class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        left = 0
        sub = set()
        for right in range(len(s)):
            while s[right] in sub:
                sub.remove(s[left])
                left+=1
            sub.add(s[right])
            count = max(right-left+1,count)
        return count
