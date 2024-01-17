from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        counter_s = Counter()
        left, right = 0, 0
        min_length = float('inf')
        min_window = ""

        while right < len(s):
            if s[right] in counter_t:
                counter_s[s[right]] += 1

            while all(counter_s[char] >= counter_t[char] for char in counter_t):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left : right + 1]

                if s[left] in counter_t:
                    counter_s[s[left]] -= 1

                left += 1

            right += 1

        return min_window