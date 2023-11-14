class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        counter = defaultdict(int)
        for i,char in enumerate(s):
            counter[char] = i
        end = 0
        size = 0
        for right in range(len(s)):
            end = max(end,counter[s[right]])
            size += 1
            if right == end:
                res.append(size)
                size = 0
        return res
