class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o','u'])
        count_vowels = 0
        ans = 0
        left = 0
        for right in range(len(s)):
            count_vowels += s[right] in vowels
            while right-left+1>k:
                count_vowels -= s[left] in vowels
                left += 1
            ans = max(ans,count_vowels)
        return ans