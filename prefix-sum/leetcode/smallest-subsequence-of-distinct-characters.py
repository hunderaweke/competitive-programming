class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter = Counter(s)
        visited = set()
        stack = []
        for i,ch in enumerate(s):
            counter[ch] -= 1
            if ch in visited:
                continue
            while stack and stack[-1] > ch and counter[stack[-1]] > 0:
                prev_char = stack.pop()
                visited.remove(prev_char)
            stack.append(ch)
            visited.add(ch)
        return "".join(stack)