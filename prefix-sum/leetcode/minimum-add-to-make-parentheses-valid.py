class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for token in s:
            if token == '(' or not stack or (stack and stack[-1] != '('):
                stack.append(token)
            else:
                stack.pop()

        return len(stack)