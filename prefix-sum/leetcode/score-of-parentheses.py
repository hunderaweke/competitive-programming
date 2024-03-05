class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for ch in s:
            if ch == ")":
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    score = 0
                    while stack[-1] != "(":
                        score += 2*stack.pop()
                    stack.pop()
                    stack.append(score)  
            else:
                stack.append(ch)
        return sum(stack)