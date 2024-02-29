class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i,ch in enumerate(s):
            last_index[ch] = i
        ans = []
        start = 0
        last = 0
        for end in range(len(s)):
            last = max(last,last_index[s[end]])
            if end == last:
                ans.append(end-start+1)
                start = end+1
        return ans