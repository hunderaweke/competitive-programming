class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        res = 0
        for right in range(len(s)):
            count[s[right]] += 1
            while count[s[right]] > 1:
                count[s[left]] -= 1
                if not count[s[left]]:
                    count.pop(s[left])
                left += 1
            res = max(res,right-left +1)
        return res