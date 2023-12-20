class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(x) for x in words)
        printed = ['']*max_len
        for word in words:
            for i in range(max_len):
                if i > len(word)-1:
                    printed[i] += " "
                else:
                    printed[i] += word[i]
        return [x.rstrip() for x in printed]