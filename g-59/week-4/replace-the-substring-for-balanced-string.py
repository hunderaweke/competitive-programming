
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        expected, got = defaultdict(int), defaultdict(int)
        for ch in "QWER":
            expected[ch] += n // 4
            got[ch] += s.count(ch)
        diff = {
            ch: got[ch] - expected[ch] for ch in "QWER" if got[ch] - expected[ch] > 0
        }
        if len(diff) == 0:
            return 0
        running_counter = defaultdict(int)
        left, right, min_length = 0, 0, float("inf")
        while right < n:
            if s[right] in diff:
                running_counter[s[right]] += 1
            while all(running_counter[char] >= diff[char] for char in diff):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                if left < n and s[left] in diff:
                    running_counter[s[left]] -= 1
                left += 1
            right += 1
        return min_length